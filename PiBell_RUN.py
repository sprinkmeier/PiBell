#!/usr/bin/env python

import RPi.GPIO as GPIO

import os
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)

while 1:
    print("rdy...")
    GPIO.wait_for_edge(26, GPIO.FALLING)
    print("PING!")
    os.system("su pi -c /home/pi/PiBell.py")
    time.sleep(30)
