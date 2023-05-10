
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def read(): # Reads RFID serial number and text associated ith
	reader = SimpleMFRC522()
	try:
		id, text = reader.read()
		print(id)
		print(text)
	finally:
		GPIO.cleanup()
	return text.strip(" ")