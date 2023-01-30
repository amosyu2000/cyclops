import RPi.GPIO as GPIO
import time
from print_handler import print_handler
from ultrasonic_sensor.led import LED
from ultrasonic_sensor.ultrasonic import Ultrasonic

class Start():
	def __init__(self, poweroff_event):
		print_handler("Thread", "Ultrasonic thread started")

		led = LED(17, 22, 23, 25, 27)
		ultrasonic = Ultrasonic(pin_trigger=18, pin_echo=24, distance_min=0, distance_max=200, unit="cm")

		while not poweroff_event.is_set():
			led.percentage_high(ultrasonic.distance_percentage())
			time.sleep(0.5)
		led.close()
		ultrasonic.close()

		print_handler("Thread", "Ultrasonic thread safely stopped")


if __name__ == '__main__':
	Start()
