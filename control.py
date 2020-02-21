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


def initialize():
    """
    """
    s = serial.Serial('/dev/cu.usbmodem14201',115200)
    # Wake up grbl
    s.write("\r\n\r\n")
    time.sleep(2)   # Wait for grbl to initialize
    execute_command(s, 'g92x0y0z0')
    return s


def execute_command(s, command):
    """
    """
    s.flushInput()  # Flush startup text in serial input
    s.write('{}\n'.format(command.strip()))
    grbl_out = s.readline()
    print 'grbl : ' + grbl_out.strip()


def move(s, nudger_distance=0, takeaway_distance=0, elevator_distance=0, speed=180):
    """
    Movement in millimeters of the first drive (nudger + retard rolls)
    """
    d1 = NUDGER_FEED_DIR*nudger_distance
    d2 = TAKEAWAY_FEED_DIR*takeaway_distance
    d3 = ELEVATOR_FEED_DIR*elevator_distance
    execute_command(s, 'f{}'.format(speed))
    execute_command(s, 'g92x0y0z0')
    execute_command(s, 'g1{}{}{}{}'.format(NUDGER_AXIS, d1,TAKEAWAY_AXIS, d2))
    execute_command(s, 'g1{}{}'.format(ELEVATOR_AXIS, d3))

def move_sheet(s):
    """
    """
    move(s, nudger_distance=3, takeaway_distance=3, elevator_distance=0.03, speed=1000)
    move(s, nudger_distance=0, takeaway_distance=3, speed=2000)
    

def move_sheets(s, sheet_count=10):
    """
    """
    for i in range(sheet_count):
        print("Feeding sheet #{}".format(i))
        move_sheet(s)


if __name__ == '__main__':
    s = initialize()
    move_sheets(s, sheet_count=1)
    # move_sheet(s)
    s.close()
    # move_sheet(s)
    # move(s, elevator_distance=0.05)