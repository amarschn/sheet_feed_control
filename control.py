"""
Description: Module for use in controlling the SAR test fixture.

Author: Drew Marschner
Date: 8/2/2020


TODO:
- Include performance % metrics in report
- Add stubs for sensor,event,etc. values for each page
- Add logging?
- Add in configuration upload to arduino capability
"""

import datetime
import json
import os
import sys

import serial


default_config = {
    "TEST_RESULTS_DIRECTORY": 'results',
    "SERIAL_PORT": "/dev/ttyACM0",
}


class SAR(object):
    """An object used to control and access the SAR/FAR test fixture."""

    def __init__(self, config):
        """Initialize SAR object with config."""
        self.config = config
        self.serial = None
        self.test_file = None
        self.test_data = None

        # Make test results directory if it does not exist
        if not os.path.exists(self.config["TEST_RESULTS_DIRECTORY"]):
            os.mkdir(self.config["TEST_RESULTS_DIRECTORY"])

    def initialize_serial(self):
        """Initialize serial connections."""
        try:
            self.serial = serial.Serial(self.config["MOTOR_SERIAL_PORT"], 115200)
        except serial.SerialException:
            print("Motor arduino unable to connect.")
            self.shut_down()

    def shut_down(self):
        """Shut down the connection to the test fixture and save test data."""
        if self.serial is not None:
            self.serial.close()
        if self.test_file is not None and self.test_data is not None:
            with open(self.test_file, 'w') as f:
                json.dump(self.test_data, f)
        sys.exit()

    def move_sheet(self):
        """Move a sheet through the SAR feeder."""
        self.serial.flushInput()
        command_string = "1\n"
        self.serial.write(str.encode(command_string))
        return self.serial.readline()

    def get_previous_user_entry(self):
        """Get previous user entry data."""
        return {}

    def collect_user_entry_data(self):
        """Collect user data about non-sensed test parameters."""
        if self.test_data is None:
            return "Test data has not been initialized."
        else:
            self.test_data['user_entry_data'] = {}

            # If this is the same as most previous test allow for copying of
            # all data
            use_previous = input(
                "If all settings are the same as the most previous test press 0, if not press any key...")
            if use_previous is '0':
                self.get_previous_user_entry()
                return

            entry = {}

            # Collect sheet type (CF or GF)
            sheet_type = input(
                "Select '1' for Carbon Fiber sheets or '2' for Fiberglass sheets...")
            if sheet_type is '1':
                entry['sheet_type'] = 'Carbon Fiber'
            elif sheet_type is '2':
                entry['sheet_type'] = 'Fiberglass'
            else:
                entry['sheet_type'] = 'Unknown'

            # Collect sheet GSM
            entry['sheet_gsm'] = input("Enter GSM value of sheet...")

            # Collect pull-off test average required normal force
            entry['pull_off_normal_force'] = input("Enter the max pull-off force result from performing the pull-off test of 10 sheets...")

            # Collect number of sheets in elevator
            entry['number_of_sheets_in_elevator'] = input("Enter the approximate number of sheets in the elevator...")

            # Collect retard clutch torque value
            entry['retard_clutch_value'] = input("Enter the retard clutch torque setting...")

            # Collect retard roll spring value
            entry['retard_spring_compression'] = input("Enter the screw distance (mm) for the spring drive screws...")

            # Collect desired number of sheets to be fed through the machine.
            # Option for "continuous" mode is default
            entry['number_of_sheets_to_feed'] = input("Enter the number of sheets to feed in this test or press Enter for continuous feed mode...")

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
            results[sheet_number] = input("Press 1 if success, 2 if multifeed, 3 if misfeed, 4 if sheet damage, 0 if the test is complete...")
            if results[sheet_number] == '0':
                break
            if not continuous:
                sheets_left -= 1
        return results

    def run_test(self):
        """Execute a test run with full data collection."""
        self.initialize_serial()
        self.test_data = {}

        # Record date
        date_string = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.test_data['date'] = date_string
        self.test_file = os.path.join(self.config["TEST_RESULTS_DIRECTORY"], date_string + ".json")
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
        try:
            self.test_data['sheet_data'] = self.feed_sheets(continuous, sheet_count)
        except Exception as e:
            print(e)
            self.shut_down()

        # Record performance data as percentages (for easier parsing of results
        # json). Not using Counter approach even though it is faster because it
        # doesn't matter for these sheet feed numbers.
        collated_results = list(self.test_data['sheet_data'].values())
        self.test_data['total_sheets_fed'] = len(collated_results)
        self.test_data['percentage_successful'] = collated_results.count('1')
        self.test_data['percentage_multifeed'] = collated_results.count('2')
        self.test_data['percentage_misfeed'] = collated_results.count('3')
        self.test_data['percentage_sheet_damage'] = collated_results.count('4')

        # Collect any extra notes (sheet processing conditions, strange events,
        # manual changes, etc.)
        notes = input("Write down any other notes, press Enter when done...")
        self.test_data['notes'] = notes

        # Shut down communication and save data
        self.shut_down()

    def move_elevator(self, z=-5):
        """Move the elevator stage down by some amount."""
        self.execute_gshield_command("g1{}{}".format(self.config["ELEVATOR_AXIS"], z))

if __name__ == '__main__':
    S = SAR(default_config)
    S.run_test()
