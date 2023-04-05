from print_handler import print_handler
from lidar_thread.lidar import Lidar
from led_handler import Led_Handler
import time
from threading import Event

class Start():
	def __init__(self, directory, poweroff_event, capture_event, led_handler):
		sample_rate = 5 # potential sample rates [1-250]
		baud_rate = 115200 # potential baudrates [9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600]
		self.lidar = Lidar(sample_rate, baud_rate)
		estimated_run_time = 0.001
		sleep_time = 1.0/(sample_rate) - estimated_run_time
		print_handler("Thread - Lidar", "Lidar thread started")

		while not poweroff_event.is_set():
			# get distance & update LEDS
			distance = int(self.lidar.read_data() or 999)
			led_handler.distance_display(distance)
			if capture_event.is_set():
				self.lidar.export_data(directory)
				capture_event.clear()
			time.sleep(sleep_time)
		
		# close the leds
		self.lidar.close()
		print_handler("Thread - Lidar", "Lidar thread safely stopped")

if __name__ == '__main__':
	Start(Event(), Event())
