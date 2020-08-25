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

NUDGER_ENGAGE_SIGNAL = 'm8'
NUDGER_DISENGAGE_SIGNAL = 'm9'

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


def initialize():
    """
    """
    sar_serial = serial.Serial('/dev/cu.usbmodem14201',115200)
    # Wake up grbl
    sar_serial.write(str.encode("\r\n\r\n"))
    time.sleep(2)   # Wait for grbl to initialize
    execute_sar_command(sar_serial, 'g91')
    # Lock the motors when not in use
    execute_sar_command(sar_serial, '$1=0')

    return sar_serial


def execute_sar_command(s, command):
    """
    """
    s.flushInput()  # Flush startup text in serial input
    command_string = '{}\n'.format(command.strip())
    s.write(str.encode(command_string))
    grbl_out = s.readline()
    # print("HI")

def engage_nudger(s):
    execute_sar_command(s, NUDGER_ENGAGE_SIGNAL)
    # s.flushInput()
    # s.write(str.encode(NUDGER_ENGAGE_SIGNAL+"\n"))
    # # grbl_out = s.readline()
    # # print(grbl_out)
    # s.flushInput()

def disengage_nudger(s):
    execute_sar_command(s, NUDGER_DISENGAGE_SIGNAL)
    # s.flushInput()
    # s.write(str.encode(NUDGER_DISENGAGE_SIGNAL+"\n"))
    # grbl_out = s.readline()
    # print(grbl_out)
    # s.flushInput()

def move_elevator(s, elevator_distance = .04):
    execute_sar_command(s, 'g1{}{}'.format(ELEVATOR_AXIS, elevator_distance))

def move_sheet(s, nudger_distance=1, feed_distance=1.75, takeaway_distance=4, elevator_distance=0.043, speed=200):
    """
    Movement in millimeters of the first drive (nudger + retard rolls)
    """
    nudge = NUDGER_FEED_DIR*nudger_distance
    feed = NUDGER_FEED_DIR*feed_distance
    takeaway = TAKEAWAY_FEED_DIR*takeaway_distance
    elevator = ELEVATOR_FEED_DIR*elevator_distance
    execute_sar_command(s, 'f{}'.format(speed))
    print("Nudge Operation")
    engage_nudger(s)
    # _ = input("Press Enter to continue...")
    execute_sar_command(s, 'g1{}{}{}{}'.format(NUDGER_AXIS, nudge,TAKEAWAY_AXIS, nudge))
    time.sleep(1)
    _ = input("Press Enter to continue...")
    print("Feed + Takeaway Operation")
    disengage_nudger(s)
    execute_sar_command(s, 'g1{}{}{}{}'.format(NUDGER_AXIS, feed, TAKEAWAY_AXIS, feed))
    execute_sar_command(s, 'g1{}{}'.format(TAKEAWAY_AXIS, takeaway))
    execute_sar_command(s, 'g1{}{}'.format(ELEVATOR_AXIS, elevator))

    time.sleep(2)
    result = input("Press 1 if success, 2 if double pick, 3 if mis-pick, 4 if sheet damage...")
    return result
    

def move_sheets(s, sheet_count=1):
    """
    """
    results = []
    for i in range(sheet_count):
        print("Feeding sheet #{}".format(i))
        result = move_sheet(s)
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
    s = initialize()
    # ipdb.set_trace()
    # test_nudger(s)
    move_sheets(s, sheet_count=10)
    # move_elevator(s)
    # execute_sar_command(s, 'g1{}{}'.format(NUDGER_AXIS, 10))
    # test_nudger(n)
    
    s.close()