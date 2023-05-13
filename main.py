from servo_test import servo_up, servo_down
from rfid_read import read
import RPi.GPIO as GPIO
# from rfid_write import write
import time
# from led import red
# from led import green
from button import pressed
# NEED TO RUN "sudo pigpiod" in console before running main.py

current = None 


while True:
    text = read()
    button = pressed()
    # Where True == Up, False == Down
    if (text == "up") and (button == False) and (current == None or current == False):
        current = True
        servo_up()
        print("UP")

    elif (button == True) and (current == True):
        current = False
        servo_down()
        print("DOWN")

    else:
        time.sleep(1)
