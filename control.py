# !/usr/bin/env python
"""
Simple g-code streaming script for grbl


To lock the motors when they are not moving: $1=255
"""

import serial
import time
import datetime
import json


NUDGER_AXIS = 'y'
TAKEAWAY_AXIS = 'z'
ELEVATOR_AXIS = 'x'

NUDGER_FEED_DIR = 1
TAKEAWAY_FEED_DIR = 1
ELEVATOR_FEED_DIR = 1

NUDGER_ENGAGE_SIGNAL = 1
NUDGER_DISENGAGE_SIGNAL = 0

MOTOR_SERIAL_PORT = "/dev/ttyACM1" #"/dev/cu.usbmodem14201"
SENSOR_SERIAL_PORT = "/dev/ttyACM0"

def run_test():
    """
    """

    test_data = {}

    # Record date
    date_string = datetime.datetime.now().strfime("%Y-%m-%d_%H:%M:%S")
    test_data['date'] = date_string

    # Collect sheet type
    sheet_type = input("Select '1' for Carbon Fiber sheets or '2' for Fiberglass sheets...")
    if sheet_type is '1':
        test_data['sheet_type'] = 'Carbon Fiber'
    elif sheet_type is '2':
        test_data['sheet_type'] = 'Fiberglass'
    else:
        test_data['sheet_type'] = 'Unknown'

    # Collect sheet-to-sheet friction average over some number of samples
    sheet_sheet_friction_average = 0

    # Collect desired number of sheets to be fed through the machine.
    # Option for "continuous" mode is default
    number_of_sheets_to_feed = 0

    # Collect number of sheets in elevator
    number_of_sheets_in_elevator = 0

    # Collect retard clutch torque value
    retard_clutch_value = 0

    # Record all configuration settings
    nudger_distance = 0
    nudger_speed = 0
    feed_distance = 0
    feed_speed = 0
    takeaway_distance = 0
    takeaway_speed = 0
    elevator_distance = 0

    # Collect any extra notes (sheet processing conditions, strange events, manual changes, etc.)
    notes = 0
    
    test_file = date_string + ".json"


def initialize_motor_serial():
    """
    """
    sar_serial = serial.Serial(MOTOR_SERIAL_PORT,115200)
    
    # Wake up grbl
    sar_serial.write(str.encode("\r\n\r\n"))
    time.sleep(2)   # Wait for grbl to initialize
    execute_sar_command(sar_serial, 'g91')
    # Lock the motors when not in use
    execute_sar_command(sar_serial, '$1=0')

    return sar_serial
    
def initialize_sensor_serial():
    sensor_serial = serial.Serial(SENSOR_SERIAL_PORT, 115200)
    return sensor_serial

def execute_sar_command(s, command):
    """
    """
    s.flushInput()  # Flush startup text in serial input
    command_string = '{}\n'.format(command.strip())
    s.write(str.encode(command_string))
    grbl_out = s.readline()
    # print("HI")

def engage_nudger(s):
    execute_sar_command(s, 'm8')
    #sensor_ser.flushInput()
    #sensor_ser.write(NUDGER_ENGAGE_SIGNAL)
    # # grbl_out = s.readline()
    # # print(grbl_out)
    #sensor_ser.flushInput()

def disengage_nudger(s):
    execute_sar_command(s, 'm9')
    #sensor_ser.flushInput()
    # sensor_ser.write(NUDGER_DISENGAGE_SIGNAL)
    # grbl_out = s.readline()
    # print(grbl_out)
    # sensor_ser.flushInput()

def nudger_too_low(sensor_ser):
    """Read nudger sensor
    """
    try:
        sensor_ser.flushInput()
        nudger_sensor = int(sensor_ser.readline())
        if nudger_sensor == 1:
            return False
        else:
            return True
    except ValueError:
        print("Value Error")
        return False
    

def check_nudger(sar_ser, sensor_ser, elevator_distance = 0.04):
    """Determine if the nudger sensor is activated
    If the nudger is activated, move the elevator up until it is not
    """
    elevator = ELEVATOR_FEED_DIR*elevator_distance
    upward_moves = 0
    while (nudger_too_low(sensor_ser) is True and upward_moves < 20):
        print("Nudger is too low, moving up #{}".format(upward_moves))
        time.sleep(0.1)
        execute_sar_command(sar_ser, "g1{}{}".format(ELEVATOR_AXIS, elevator))
        upward_moves+=1


def move_elevator(s, elevator_distance = 0.04):
    execute_sar_command(s, 'g1{}{}'.format(ELEVATOR_AXIS, elevator_distance))

def move_sheet(sar_ser, sensor_ser, nudger_distance=1, feed_distance=1.75, takeaway_distance=4, elevator_distance=0.043, speed=200):
    """
    Movement in millimeters of the first drive (nudger + retard rolls)
    """
    nudge = NUDGER_FEED_DIR*nudger_distance
    feed = NUDGER_FEED_DIR*feed_distance
    takeaway = TAKEAWAY_FEED_DIR*takeaway_distance
    elevator = ELEVATOR_FEED_DIR*elevator_distance
    execute_sar_command(sar_ser, 'f{}'.format(speed))
    
    print("Nudge Operation")
    engage_nudger(sar_ser)
    
    print("Checking Nudger")
    time.sleep(1.0)
    check_nudger(sar_ser, sensor_ser)
    
    # _ = input("Press Enter to continue...")
    execute_sar_command(sar_ser, 'g1{}{}{}{}'.format(NUDGER_AXIS, nudge,TAKEAWAY_AXIS, nudge))
    time.sleep(1)
    _ = input("Press Enter to continue...")
    print("Feed + Takeaway Operation")
    disengage_nudger(sar_ser)
    execute_sar_command(sar_ser, 'g1{}{}{}{}'.format(NUDGER_AXIS, feed, TAKEAWAY_AXIS, feed))
    execute_sar_command(sar_ser, 'g1{}{}'.format(TAKEAWAY_AXIS, takeaway))
    execute_sar_command(sar_ser, 'g1{}{}'.format(ELEVATOR_AXIS, elevator))

    time.sleep(2)
    result = input("Press 1 if success, 2 if double pick, 3 if mis-pick, 4 if sheet damage...")
    return result
    

def move_sheets(sar_ser, sensor_ser, sheet_count=1):
    """
    """
    results = []
    for i in range(sheet_count):
        print("Feeding sheet #{}".format(i))
        result = move_sheet(sar_ser, sensor_ser)
        results.append(result)
    print(results)

def test_nudger(s):
    wait_time = 1.0
    for i in range(5):
        engage_nudger(s)
        time.sleep(wait_time)
        disengage_nudger(s)
        time.sleep(wait_time)

if __name__ == '__main__':
    sar_ser = initialize_motor_serial()
    sensor_ser = initialize_sensor_serial()
    #check_nudger(sar_ser, sensor_ser)
    #test_nudger(sar_ser)
    #ipdb.set_trace()
    # test_nudger(s)
    move_sheets(sar_ser, sensor_ser, sheet_count=2)
    # move_elevator(s)
    # execute_sar_command(s, 'g1{}{}'.format(NUDGER_AXIS, 10))
    # test_nudger(n)
    sar_ser.close()
    sensor_ser.close()
