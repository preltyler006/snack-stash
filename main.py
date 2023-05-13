from servo_test import servo_up, servo_down
from rfid_read import read
# from rfid_write import write
import time
# from led import red
# from led import green

current = None 

while True:
    text = read()
    # Where True == Up, False == Down
    if text == "white" and (current == None or current == False):
        servo_up()
        print("UP")
        current = True
    elif text == "white" and (current == True):
        servo_down()
        print("DOWN")
        current = False
    else:
        time.sleep(1)
