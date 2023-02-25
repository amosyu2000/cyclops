import RPi.GPIO as GPIO
import time
from threading import Event
from print_handler import print_handler
from ultrasonic_thread.led import LED
from ultrasonic_thread.ultrasonic import Ultrasonic

class Start():
	def __init__(self, poweroff_event, capture_event):
		try:
			print_handler("Thread - Lidar", "Lidar thread started")

			while not poweroff_event.is_set():
				# get distance & update LEDS
				time.sleep(0.2)
			
			#self.led.close()
			self.lidar.close()
			print_handler("Thread - Lidar", "Lidar thread safely stopped")
		except:
			print_handler("Thread - Lidar", "Error. The lidar modules has failed!")

if __name__ == '__main__':
	Start(Event(), Event())
