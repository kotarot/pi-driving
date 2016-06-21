#!/usr/bin/env python

import RPi.GPIO as GPIO

PIN1 = 11
PIN2 = 13
PIN3 = 19
PIN4 = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN1, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)
GPIO.setup(PIN3, GPIO.OUT)
GPIO.setup(PIN4, GPIO.OUT)

while True:
    GPIO.output(PIN2, False)
    GPIO.output(PIN1, True)
    GPIO.output(PIN4, False)
    GPIO.output(PIN3, True)
