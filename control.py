"""
Description: Module for use in controlling the SAR test fixture.

Author: Drew Marschner
Date: 8/2/2020

Notes:
- Hi

TODO:
- Implement class for SAR fixture
- Implement test run export functionality
"""

import serial
import time
import datetime
import json
import os

default_config = {
    "TEST_RESULTS_DIRECTORY": 'results',
    "NUDGER_AXIS": 'y',
    "TAKEAWAY_AXIS": 'z',
    "ELEVATOR_AXIS": 'x',
    "NUDGER_ENGAGE_SIGNAL": 1,
    "NUDGER_DISENGAGE_SIGNAL": 0,
    "MOTOR_SERIAL_PORT": "/dev/ttyACM1",
    "SENSOR_SERIAL_PORT": "/dev/ttyACM0",
    "ELEVATOR_FEED_DISTANCE": 0.043,
    "NUDGER_FEED_DISTANCE": 1,
    "FEEDER_FEED_DISTANCE": 1.75,
    "TAKEAWAY_FEED_DISTANCE": 4,
    "MOTOR_SPEED": 200
}


class SAR(object):
    """An object used to control and access the SAR/FAR test fixture."""

    def __init__(self, config):
        """Initialize SAR object with config."""
        self.config = config
        self.motor_serial = None
        self.sensor_serial = None
        self.test_file = None
        self.test_data = None

        # Make test results directory if it does not exist
        if not os.path.exists(self.config["TEST_RESULTS_DIRECTORY"]):
            os.makedir(self.config["TEST_RESULTS_DIRECTORY"])

    def initialize_motor_serial(self):
        """Initialize the serial connection the gshield."""
        self.motor_serial = serial.Serial(
            self.config["MOTOR_SERIAL_PORT"], 115200)
        # Wake up grbl
        self.motor_serial.write(str.encode("\r\n\r\n"))
        time.sleep(2)   # Wait for grbl to initialize
        self.execute_gshield_command(self.motor_serial, 'g91')
        self.motor_lock(False)
        self.execute_gshield_command('f{}'.format(self.config["MOTOR_SPEED"]))

    def shut_down(self):
        """Shut down the connection to the test fixture and save test data."""
        if self.motor_serial is not None:
            self.motor_serial.close()
        if self.sensor_serial is not None:
            self.sensor_serial.close()
        if self.test_file is not None and self.test_data is not None:
            with open(self.test_file, 'w') as f:
                json.dump(self.test_data, f)

    def motor_lock(self, val=False):
        """Lock the motors when not in use if True."""
        if val:
            command = 255
        else:
            command = 0
        self.execute_gshield_command(
            self.motor_serial, '$1={}'.format(command))

    def initialize_sensor_serial(self):
        """Initialize the serial connection with the sensor arduino board."""
        self.sensor_serial = serial.Serial(
            self.config["SENSOR_SERIAL_PORT"], 115200)

    def execute_gshield_command(self, command):
        """Execute a motor command on the gshield board."""
        self.motor_serial.flushInput()  # Flush startup text in serial input
        command_string = '{}\n'.format(command.strip())
        self.motor_serial.write(str.encode(command_string))
        return self.motor_serial.readline()

    def engage_nudger(self):
        """Engage the nudger servo."""
        self.execute_gshield_command('m8')

    def disengage_nudger(self):
        """Disengage the nudger servo."""
        self.execute_gshield_command('m9')

    def nudger_too_low(self):
        """Read nudger switch value.

        Returns True if the switch is depressed and false if not.
        """
        try:
            self.sensor_serial.flushInput()
            nudger_sensor = int(self.sensor_serial.readline())
            if nudger_sensor == 1:
                return False
            else:
                return True
        except ValueError:
            print("Value Error")
            return False

    def check_nudger(self):
        """Determine if the nudger sensor is activated.

        If the nudger is activated, move the elevator up until it is not
        """
        elevator = self.config["ELEVATOR_FEED_DISTANCE"]
        upward_moves = 0

        while (self.nudger_too_low() is True and upward_moves < 20):
            print("Nudger is too low, moving up #{}".format(upward_moves))
            time.sleep(0.1)
            self.execute_gshield_command(
                "g1{}{}".format(self.config["ELEVATOR_AXIS"], elevator))
            upward_moves += 1

    def test_nudger(self, up_downs=5, delay_time=1.0):
        """Test nudger up and down."""
        for i in range(up_downs):
            self.engage_nudger()
            time.sleep(delay_time)
            self.disengage_nudger()
            time.sleep(delay_time)

    def nudge(self):
        """Acquire a sheet onto the feed roll."""
        axis = self.config["NUDGER_AXIS"]
        feed = self.config["NUDGER_FEED_DISTANCE"]
        print("Nudge Operation...")
        self.engage_nudger()
        print("Checking Nudger...")
        time.sleep(1.0)
        self.check_nudger()
        self.execute_gshield_command('g1{}{}{}{}'.format(axis, feed))

    def feed_takeaway(self):
        """Move a sheet through the feed + takeaway."""
        n_axis = self.config["NUDGER_AXIS"]
        t_axis = self.config["TAKEAWAY_AXIS"]
        e_axis = self.config["ELEVATOR_AXIS"]
        f1 = self.config["FEEDER_FEED_DISTANCE"]
        f2 = self.config["TAKEAWAY_FEED_DISTANCE"]
        f3 = self.config["ELEVATOR_FEED_DISTANCE"]
        self.disengage_nudger()
        self.execute_gshield_command('g1{}{}{}{}'.format(n_axis, f1, t_axis, f1))
        self.execute_gshield_command('g1{}{}'.format(t_axis, f2))
        # Raise the elevator for the next sheet
        self.execute_gshield_command('g1{}{}'.format(e_axis, f3))
        time.sleep(1)

    def move_sheet(self):
        """Move a sheet through the SAR feeder."""
        self.nudge()
        time.sleep(1)
        input("Press Enter to continue...")
        print("Feed + Takeaway Operation")
        self.feed_takeaway()

    def collect_user_entry_data(self):
        """Collect user data about non-sensed test parameters."""
        if self.test_data is None:
            return "Test data has not been initialized."
        else:
            self.test_data['user_entry_data'] = {}

            # If this is the same as most previous test allow for copying of
            # all data
            use_previous = input(
                "If all settings are the same as the most previous test press 0\
                , if not press any key...")
            if use_previous is '0':
                self.get_previous_data_config()
                return

            entry = {}

            # Collect sheet type (CF or GF)
            sheet_type = input(
                "Select '1' for Carbon Fiber sheets or '2' for \
                Fiberglass sheets...")
            if sheet_type is '1':
                entry['sheet_type'] = 'Carbon Fiber'
            elif sheet_type is '2':
                entry['sheet_type'] = 'Fiberglass'
            else:
                entry['sheet_type'] = 'Unknown'

            # Collect sheet GSM
            entry['sheet_gsm'] = input("Enter GSM value of sheet...")

            # Collect pull-off test average required normal force
            entry['pull_off_normal_force'] = input("Enter the average normal\
                    force used in a pull-off test of 10 sheets...")

            # Collect desired number of sheets to be fed through the machine.
            # Option for "continuous" mode is default
            entry['number_of_sheets_to_feed'] = input("Enter the number of\
                sheets to feed in this test or press Enter for continuous \
                feed mode...")

            # Collect number of sheets in elevator
            entry['number_of_sheets_in_elevator'] = input("Enter the approximate number\
                 of sheets in the elevator...")

            # Collect retard clutch torque value
            entry['retard_clutch_value'] = input("Enter the retard clutch torque \
                setting...")

            # Collect retard roll spring value
            entry['retard_spring_compression'] = input("Enter the screw distance for the \
                spring drive screws...")

            # Record entry data in test data dict
            self.test_data['user_entry_data'] = entry

    def feed_sheets(self, continuous=True, sheets_left=1):
        """Feed sheets and return results dict."""
        results = {}
        sheet_number = 0
        while(sheets_left > 0):
            print("Feeding sheet #{}".format(sheet_number))
            self.move_sheet()
            sheet_number += 1
            results[sheet_number] = input("Press 1 if success, 2 if double pick, 3 if mis-pick, \
                4 if sheet damage, 0 if the test is complete...")
            if results[sheet_number] == '0':
                break
            if not continuous:
                sheets_left -= 1
        return results

    def run_test(self):
        """Execute a test run with full data collection."""
        self.test_data = {}

        # Record date
        date_string = datetime.datetime.now().strfime("%Y-%m-%d_%H:%M:%S")
        self.test_data['date'] = date_string
        self.test_file = date_string + ".json"
        self.collect_user_entry_data()

        # Record all configuration settings
        self.test_data['config'] = self.config

        self.test_data['sheet_data'] = {}
        sheet_count = self.test_data['user_entry_data']['number_of_sheets_to_feed']
        if sheet_count == '':
            continuous = True
            sheet_count = 1
        else:
            sheet_count = int(sheet_count)
            continuous = False

        # Feed sheets, collecting user input data for each sheet
        self.test_data['sheet_data'] = self.feed_sheets(continuous, sheet_count)

        # Collect any extra notes (sheet processing conditions, strange events,
        # manual changes, etc.)
        notes = input("Write down any other notes, press Enter when done...")
        self.test_data['notes'] = notes

        # Shut down communication and save data
        self.shut_down()


if __name__ == '__main__':
    S = SAR(default_config)
    S.run_test()
