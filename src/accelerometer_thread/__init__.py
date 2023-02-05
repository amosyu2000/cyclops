import board
import busio
import time
from threading import Event
from accelerometer_thread.acceleration import Acceleration
from accelerometer_thread.acceleration_plot import Acceleration_Plot
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event, crash_event, capture_event):
		print_handler("Thread", "Acceleration thread started")

		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.acceleration = Acceleration(i2c=self.i2c, average_of=3)

		while not poweroff_event.is_set():
			self.acceleration.temp_log()
			if capture_event.is_set():
				self.acceleration.export_log()
				capture_event.clear()
			time.sleep(1)

		self.acceleration.close()

		print_handler("Thread", "Acceleration thread safely stopped")

class Start_Plot:
	def __init__(self, poweroff_event):
		print_handler("Thread", "Acceleration plot thread started")

		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.acceleration = Acceleration(i2c=self.i2c, average_of=3)

		self.acceleration_plot = Acceleration_Plot(acceleration=self.acceleration, data_points=50)

		while not poweroff_event.is_set():
			self.acceleration_plot.update()
			self.acceleration_plot.pause(1)

		self.acceleration_plot.close()

		print_handler("Thread", "Acceleration thread safely stopped")

if __name__ == '__main__':
	#Start(Event(), Event(), Event())
	Start_Plot(Event())
