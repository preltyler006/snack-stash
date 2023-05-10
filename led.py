import RPi.GPIO as GPIO
import random as rand
import tkinter as tk
import time

# GPIO.setmode(GPIO.BCM) # Allows you to use GPIO numbers and not raspberry pi pin number, much easier
GREEN_LED = 17

def green():
    GPIO.setup(GREEN_LED, GPIO.OUT) # Sets GPIO Pin 17 to output mode so we can control the pin
    GPIO.output(GREEN_LED, 1) # 1 == ON, 0 == OFF
    time.sleep(1)
    GPIO.output(GREEN_LED, 0)
    GPIO.cleanup() # Restarts GPIO pin settings, good practice for end of program