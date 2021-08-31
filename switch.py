import RPi.GPIO as GPIO
from time import sleep

DELAY = 0.1
SWITCH_PIN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	print(GPIO.input(SWITCH_PIN))
	sleep(DELAY)
