
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# GPIO.setmode(GPIO.BCM)

def read(): # Reads RFID serial number and text associated ith
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
	finally:
		GPIO.cleanup()
	return text.strip(" ")