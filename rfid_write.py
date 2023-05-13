import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def write():
	try:
		text = input("enter data to write")
		print("place your tag to write: ")
		reader.write(text)
		print("Write Successfull")
	finally:
		GPIO.cleanup()
