import RPi.GPIO as GPIO
import subprocess

GPIO.setmode(GPIO.BCM)
batPin = 17
GPIO.setup(batPin, GPIO.IN)
while True:
	if not GPIO.input(batPin):
		print("Low Battery")
		print("Shutting Down")
		subprocess.call(["sudo", "shutdown", "-h", "now"])

