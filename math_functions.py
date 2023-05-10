from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory # Lots of hardware based timing, more accurate
import math

'''
run "sudo pigpiod" before starting in the background
servo.value = degrees specified for setting exact value
'''

factory1 = PiGPIOFactory()

servo1 = Servo(17, min_pulse_width=0.9/1000, max_pulse_width=2.5/1000, pin_factory=factory1)

while True:
	for i in range(0, 360):
		servo1.value = math.sin(math.radians(i))
		sleep(0.003)
