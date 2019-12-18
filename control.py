#!/usr/bin/env python
"""\
Simple g-code streaming script for grbl
"""

import serial
import time

FIRST_DRIVE_AXIS = 'y'
SECOND_DRIVE_AXIS = 'z'

def initialize():
	s = serial.Serial('/dev/cu.usbmodem14201',115200)
	# Wake up grbl
	s.write("\r\n\r\n")
	time.sleep(2)   # Wait for grbl to initialize
	execute_command(s, 'g92y0z0')
	return s


def execute_command(s, command):
	s.flushInput()  # Flush startup text in serial input
	s.write('{}\n'.format(command.strip()))
	grbl_out = s.readline()
	print 'grbl : ' + grbl_out.strip()


def move(s, first_drive_distance=0, second_drive_distance=0, speed=180):
	"""
	Movement in millimeters of the first drive (nudger + retard rolls)
	"""
	d1 = -first_drive_distance
	d2 = -second_drive_distance
	execute_command(s, 'f{}'.format(speed))
	execute_command(s, 'g92y0z0')
	execute_command(s, 'g1{}{}{}{}'.format(FIRST_DRIVE_AXIS,
										   d1,
										   SECOND_DRIVE_AXIS,
										   d2))


def move_sheet():
	s = initialize()
	move(s, 2, 2)
	move(s, 0, 5, 400)
	s.close()



if __name__ == '__main__':
	
	move_sheet()