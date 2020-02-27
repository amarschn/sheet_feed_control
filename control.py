#!/usr/bin/env python
"""
Simple g-code streaming script for grbl
"""

import serial
import time

NUDGER_AXIS = 'y'
TAKEAWAY_AXIS = 'z'
ELEVATOR_AXIS = 'x'

NUDGER_FEED_DIR = 1
TAKEAWAY_FEED_DIR = 1
ELEVATOR_FEED_DIR = 1

NUDGER_ENGAGE_SIGNAL = '1'
NUDGER_DISENGAGE_SIGNAL = '0'

def initialize():
    """
    """
    sar_serial = serial.Serial('/dev/cu.usbmodem14201',115200)
    nudger_serial = serial.Serial('/dev/cu.usbmodem14101',115200)
    # Wake up grbl
    sar_serial.write("\r\n\r\n")
    time.sleep(2)   # Wait for grbl to initialize
    execute_sar_command(sar_serial, 'g91')
    return sar_serial, nudger_serial


def execute_sar_command(s, command):
    """
    """
    s.flushInput()  # Flush startup text in serial input
    s.write('{}\n'.format(command.strip()))
    grbl_out = s.readline()
    print 'grbl : ' + grbl_out.strip()
    # print("HI")

def engage_nudger(n):
    n.write(NUDGER_ENGAGE_SIGNAL)
    n.flushInput()

def disengage_nudger(n):
    n.write(NUDGER_DISENGAGE_SIGNAL)
    n.flushInput()

def move_sheet(s, n, nudger_distance=1, feed_distance=1.5, takeaway_distance=4, elevator_distance=0.07, speed=200):
    """
    Movement in millimeters of the first drive (nudger + retard rolls)
    """
    nudge = NUDGER_FEED_DIR*nudger_distance
    feed = NUDGER_FEED_DIR*feed_distance
    takeaway = TAKEAWAY_FEED_DIR*takeaway_distance
    elevator = ELEVATOR_FEED_DIR*elevator_distance
    execute_sar_command(s, 'f{}'.format(speed))
    print("Nudge Operation")
    engage_nudger(n)
    execute_sar_command(s, 'g1{}{}{}{}'.format(NUDGER_AXIS, nudge,TAKEAWAY_AXIS, nudge))
    time.sleep(1)
    print("Feed + Takeaway Operation")
    disengage_nudger(n)
    execute_sar_command(s, 'g1{}{}{}{}'.format(NUDGER_AXIS, feed, TAKEAWAY_AXIS, feed))
    execute_sar_command(s, 'g1{}{}'.format(TAKEAWAY_AXIS, takeaway))
    execute_sar_command(s, 'g1{}{}'.format(ELEVATOR_AXIS, elevator))
    time.sleep(2)

# def move_sheet(s):
#     """
#     """
#     move(s, nudger_distance=3, takeaway_distance=3, elevator_distance=0.03, speed=1000)
    # move(s, nudger_distance=0, takeaway_distance=3, speed=2000)
    

def move_sheets(s, n, sheet_count=10):
    """
    """
    for i in range(sheet_count):
        print("Feeding sheet #{}".format(i))
        move_sheet(s, n)

def test_nudger(n):
    for i in range(10):
        engage_nudger(n)
        time.sleep(0.1)
        disengage_nudger(n)
        time.sleep(0.1)


if __name__ == '__main__':
    s, n = initialize()
    move_sheets(s, n, sheet_count=10)
    # execute_sar_command(s, 'g1{}{}'.format(NUDGER_AXIS, 10))
    # test_nudger(n)
    
    s.close()
    n.close()