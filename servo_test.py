from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory # Lots of hardware based timing, more accurate
import RPi.GPIO as GPIO
import math


'''
run "sudo pigpiod" before starting in the background
servo.value = degrees specified for setting exact value
'''

factory1 = PiGPIOFactory()

servo1 = Servo(17, min_pulse_width=0.9/1000, max_pulse_width=2.5/1000, pin_factory=factory1)

def servo_up():
	try:
		for i in range(180, 270):
			servo1.value = math.sin(math.radians(i))
			sleep(0.01)
	except KeyboardInterrupt:
		GPIO.cleanup() # Restarts GPIO pin settings, good practice for end of program

def servo_down():
	try:
		for i in range(270, 360):
			servo1.value = math.sin(math.radians(i))
			sleep(0.01)
	except KeyboardInterrupt:
		GPIO.cleanup() # Restarts GPIO pin settings, good practice for end of program

