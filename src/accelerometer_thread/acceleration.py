import adafruit_adxl34x
import numpy as np
from statistics import fmean
import time
from csv_handler import CSV_Handler
from print_handler import print_handler

class Acceleration:
	def __init__(self, i2c, average_of=1):
		"""
		Create a class for collecting, storing, and analyzing acceleration data

		@i2c: A busio.I2C class
		@average_of: Takes a rolling average of the xyz acceleration points
		"""

		self.accelerometer = adafruit_adxl34x.ADXL345(i2c)
		self.average_of = average_of

		self.raw_x = [0] * self.average_of
		self.raw_y = [0] * self.average_of
		self.raw_z = [0] * self.average_of
		self.raw_norm = [0] * self.average_of
		self.avg_x = 0
		self.avg_y = 0
		self.avg_z = 0
		self.avg_norm = 0

		self.csv_handler = CSV_Handler("accelerometer")
		self.csv_handler.open()

	def read(self):
		"""
		Take acceleration and time readings from the ADXL345 accelerometer

		returns: new x, y, z, norm, and time readings
		"""

		[x,y,z] = self.accelerometer.acceleration
		print_handler("Acceleration", f"Readings of ({x}, {y}, {z})")
		norm = np.linalg.norm([x,y,z])

		self.raw_x.append(x)
		self.raw_y.append(y)
		self.raw_z.append(z)
		self.raw_norm.append(norm)

		self.raw_x.pop(0)
		self.raw_y.pop(0)
		self.raw_z.pop(0)
		self.raw_norm.pop(0)

		self.avg_x = fmean(self.raw_x)
		self.avg_y = fmean(self.raw_y)
		self.avg_z = fmean(self.raw_z)
		self.avg_norm = fmean(self.raw_norm)

		return [x,y,z,norm]
	
	def temp_log(self):
		"""
		Take readings and dump them in a temporary log file
		"""

		self.csv_handler.writerow(self.read())

	def export_log(self):
		"""
		Save the last x seconds of acceleration data to its own csv file
		"""

		self.csv_handler.export_latest(seconds=60)

	def close(self):
		"""
		Close the log file
		"""

		self.csv_handler.close()

	def get_avg_x(self):
		return self.avg_x

	def get_avg_y(self):
		return self.avg_y

	def get_avg_z(self):
		return self.avg_z

	def get_avg_norm(self):
		return self.avg_norm