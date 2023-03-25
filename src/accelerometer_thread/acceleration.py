import adafruit_adxl34x, time, queue, csv
import numpy as np
from statistics import fmean
from print_handler import print_handler
from dir_handler import Dir_Handler

class Acceleration:
	def __init__(self, sample_rate, i2c):
		"""
		Create a class for collecting, storing, and analyzing acceleration data

		@i2c: A busio.I2C class
		"""

		self.accelerometer = adafruit_adxl34x.ADXL345(i2c)
		self.accelerometer_data = queue.Queue(60*sample_rate) # retain last 60 econds of data
		self.dir_handler = Dir_Handler() # access most recent output directory

		# Axis Calibration
		self.xyz_scaling_factors = [1.0, 1.0, 1.0]
		self.x = 0
		self.y = 0
		self.z = 0
		self.xy_norm = 0
		self.xyz_norm = 0

	def display_scaling_factor():
		print()

	def read_data(self):
		"""
		Take acceleration and time readings from the ADXL345 accelerometer

		returns: new x, y, z, norm, and time readings
		"""
		[self.x, self.y, self.z] = [a*b for a, b in zip(self.accelerometer.acceleration, self.xyz_scaling_factors)]

		self.xy_norm = (self.x**2 + self.y**2)**0.5	# vector plane parrallel to ground
		self.xyz_norm = (self.x**2 + self.y**2 + self.z**2)**0.5

		if self.accelerometer_data.full():
			self.accelerometer_data.get()
		self.accelerometer_data.put([time.time(), self.x, self.y, self.z, self.xyz_norm])

	def is_crashed(self):
		if self.xyz_norm / 9.81 > 3:
			return True
		else:
			return False

	def export_data(self):
		"""
		Save the last x seconds of acceleration data to its own csv file
		"""
		try:
			output_directory = self.dir_handler.locate_export_dir('accelerometer')
			output_file_name = '/accelerometer_' + time.strftime('%Y-%m-%d_%H:%M:%S') + ".csv"
			with open(output_directory + output_file_name, 'w') as csv_file:
				writer = csv.writer(csv_file, delimiter=',')
				writer.writerow(['Time', 'X', 'Y', 'Z', 'Norm'])
				while not self.accelerometer_data.empty():
					writer.writerow(self.accelerometer_data.get())
			csv_file.close
		except:
			print_handler("Thread - Acceleration", "An error occured while saving the data at: " + output_directory + output_file_name)
		else:
			print_handler("Thread - Acceleration", "Saved last 60 seconds of data to: " + output_directory + output_file_name)

	def close(self):
		"""
		Close the log file
		"""
		self.accelerometer_data.empty()