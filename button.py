import RPi.GPIO as GPIO
import time


def pressed():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.IN)

    button = GPIO.input(13)
    try:
        if button == GPIO.LOW: #Press
            print("pressed")
            return True
            
    finally:
        if button == GPIO.HIGH: #NotPress
            print("not pressed")
            return False

GPIO.cleanup()