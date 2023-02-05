import RPi.GPIO as GPIO
import time
from threading import Event
from print_handler import print_handler
from ultrasonic_thread.led import LED
from ultrasonic_thread.ultrasonic import Ultrasonic

class Start():
	def __init__(self, poweroff_event, capture_event):
		print_handler("Thread", "Ultrasonic thread started")

		self.led = LED(17, 22, 23, 25, 27)
		self.ultrasonic = Ultrasonic(pin_trigger=18, pin_echo=24, distance_min=0, distance_max=200, unit="cm")

		while not poweroff_event.is_set():
			self.led.percentage_high(self.ultrasonic.distance_percentage())
			if capture_event.is_set():
				self.ultrasonic.export_log()
				capture_event.clear()
			time.sleep(0.5)
		self.led.close()
		self.ultrasonic.close()

		print_handler("Thread", "Ultrasonic thread safely stopped")


if __name__ == '__main__':
	Start(Event(), Event())
