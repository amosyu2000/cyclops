import board
import busio
import time
from accelerometer.acceleration import Acceleration
from accelerometer.acceleration_plot import Acceleration_Plot
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event):
		print_handler("Thread", "Acceleration thread started")

		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.acceleration = Acceleration(i2c=self.i2c, average_of=3)

		show_plot = False
		period = 1

		if show_plot:
			self.acceleration_plot = Acceleration_Plot(acceleration=self.acceleration, data_points=50)
			while not poweroff_event.is_set():
				self.acceleration_plot.update()
				self.acceleration_plot.pause(period)
			self.acceleration_plot.close()

		else:
			while not poweroff_event.is_set():
				self.acceleration.temp_log()
				time.sleep(period)
			self.acceleration.close()

		print_handler("Thread", "Acceleration thread safely stopped")

if __name__ == '__main__':
	Start()
