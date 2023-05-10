import os
os.system('sudo pigpiod')
from servo_test import servo_up, servo_down
from rfid_read import read
from rfid_write import write
import time
# from led import red
# from led import green

current = None 

while True:
    text = read()
    # Where True == Up, False == Down
    if text == "blue" and (current == None or current == False):
        current = True
        servo_up()
        print("UP")
    elif text == "white" and (current == True):
        current = False
        servo_down()
        print("DOWN")
    else:
        time.sleep(1)
