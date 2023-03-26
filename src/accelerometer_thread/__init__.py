import board
import busio
import time
from threading import Event
from accelerometer_thread.acceleration import Acceleration
# from accelerometer_thread.acceleration_plot import Acceleration_Plot
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event, log_event, capture_event):
		print_handler("Thread - Acceleration", "Acceleration thread started")
		self.i2c = busio.I2C(board.SCL, board.SDA)
		sample_rate = 5 # hz
		loop_time = 1.0/sample_rate
		self.acceleration = Acceleration(sample_rate, i2c=self.i2c)
		temp_flag = False

		while not poweroff_event.is_set():
			start_time = time.time()
			if capture_event.is_set():
				self.acceleration.export_data()
				capture_event.clear()
			self.acceleration.read_data()
			if temp_flag == False:
				if self.acceleration.is_crashed(): 
					print_handler("Thread - Acceleration", "Crash Detected!")
					acceleration_event_time = time.time()
					temp_flag = True
			elif time.time() - acceleration_event_time > 10:
				log_event.set()
				temp_flag = False


			sleep_time = loop_time - (time.time()-start_time)
			if sleep_time > 0:
				time.sleep(sleep_time)

		self.acceleration.close()
		print_handler("Thread - Acceleration", "Acceleration thread safely stopped")

if __name__ == '__main__':
	Start(Event(), Event(), Event())
