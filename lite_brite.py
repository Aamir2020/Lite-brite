import time
import board
import neopixel
import RPi.GPIO as GPIO

pixel_pin = board.D18

num_pixels = 4

ORDER=neopixel.RGB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
		
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(23) == 0:
		pixels.fill((255, 0, 0))
	else:
		pixels.fill((0, 0, 0))
	pixels.show()
	time.sleep(0.001)
