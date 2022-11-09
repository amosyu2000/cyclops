import adafruit_adxl34x
import board
import busio
import time
from acceleration_plot import Acceleration_Plot

class Live_Plot:
	def __init__(self):
		self.i2c = busio.I2C(board.SCL, board.SDA)
		self.accelerometer = adafruit_adxl34x.ADXL345(self.i2c)
		self.acceleration_plot = Acceleration_Plot(data_points=50, average_of=3)

		while True:
			self.acceleration_plot.update(*self.accelerometer.acceleration, time.time())
			self.acceleration_plot.pause(0.1)

if __name__ == '__main__':
	Live_Plot()
	