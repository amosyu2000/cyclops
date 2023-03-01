import RPi.GPIO as GPIO
from print_handler import print_handler
from lidar_thread.lidar import Lidar
import time
from threading import Event

class Start():
	def __init__(self, poweroff_event, capture_event):
		sample_rate = 5 # potential sample rates [1-250]
		baud_rate = 115200 # potential baudrates [9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
		self.lidar = Lidar(sample_rate, baud_rate)
		sleep_time = 1.0/(sample_rate+1)

		try:
			print_handler("Thread - Lidar", "Lidar thread started")

			while not poweroff_event.is_set():
				# get distance & update LEDS
				distance = self.lidar.read_data()
				# update the leds
				if capture_event.is_set():
					self.lidar.export_data()
					capture_event.clear()
				time.sleep(sleep_time)
			
			# close the leds
			self.lidar.close()
			print_handler("Thread - Lidar", "Lidar thread safely stopped")
		except:
			print_handler("Thread - Lidar", "Error. The lidar module has failed!")

if __name__ == '__main__':
	Start(Event(), Event())
