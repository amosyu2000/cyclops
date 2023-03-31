import adafruit_adxl34x, time, queue, csv
import numpy as np
from enum import Enum
from statistics import fmean
from print_handler import print_handler

class Acceleration:
	def __init__(self, sample_rate, i2c):
		"""
		Create a class for collecting, storing, and analyzing acceleration data

		@i2c: A busio.I2C class
		"""
		self.sample_rate = sample_rate
		self.accelerometer = adafruit_adxl34x.ADXL345(i2c)
		self.accelerometer_data = queue.Queue(60*self.sample_rate) # retain last 60 econds of data

		# Axis Calibration
		self.xyz_range = [ [-12.1, 10.1], [-13.3, 9.4], [-13.8, 8.1] ]
		self.x = 0
		self.y = 0
		self.z = 0
		self.xz_norm = 0
		self.xyz_norm = 0

		# Crash Detection
		self.state = State.NORMAL
		self.transition_state = None
		self.transition = 0

	def read_data(self):
		"""
		Take acceleration and time readings from the ADXL345 accelerometer

		returns: new x, y, z, norm, and time readings
		"""
		[self.x, self.y, self.z] = [ (a-b[0])/(b[1]-b[0])*9.81*2-9.81 for a,b in zip(self.accelerometer.acceleration, self.xyz_range)]

		self.xz_norm = (self.x**2 + self.z**2)**0.5	# vector plane parrallel to ground
		self.xyz_norm = (self.x**2 + self.y**2 + self.z**2)**0.5

		if self.accelerometer_data.full():
			self.accelerometer_data.get()
		self.accelerometer_data.put([time.time(), self.x, self.y, self.z, self.xyz_norm])

	def is_crashed(self, upright_threshold, climax_threshold, smoothing):
		"""
		State-transition algorithm for detecting a crash

		@upright_threshold: value in m/s^2 for determining when a certain axis is upright to the ground
		@climax_threshold: value in m/s^2 for the maximum g-force experienced during a crash
		@smoothing: time in seconds to wait between state transitions

		returns: True if a complete crash occurred, False otherwise
		"""
		# in seconds
		transition_threshold = smoothing * self.sample_rate

		# Get the current state of the bicycle
		current_state = None
		if self.y > upright_threshold:
			current_state = State.NORMAL
		# Immediately switch the state of the algorithm if the climax acceleration was reached
		elif self.xyz_norm > climax_threshold:
			print_handler("Thread - Acceleration", f"{self.state} -> {State.CLIMAX}")
			self.state = State.CLIMAX
			self.transition = 0
			return False
		elif self.xz_norm > upright_threshold:
			current_state = State.INVERSE
		else:
			return False

		if self.transition == 0:
			self.transition_state = current_state

		# The algorithm waits for some time before it is sure that there should be state change
		# Increase the "transition" counter by 1 every time the current state matches the transition state
		if self.transition_state == current_state:
			self.transition += 1
		# Decrease the "transition" counter by 1 every time the current state differs from the transition state
		else:
			self.transition -= 1

		# Reset the "transition" counter if there is no transition happening
		if self.state == self.transition_state:
			self.transition = 0

		# If the "transition" counter hits the transition threshold
		if self.transition >= transition_threshold:
			self.transition = transition_threshold
			# Only transition to the next state if it is valid (check the finite state diagram)
			if (
				(self.state == State.CLIMAX and self.transition_state == State.NORMAL) or
				(self.state == State.CLIMAX and self.transition_state == State.INVERSE) or
				(self.state == State.INVERSE and self.transition_state == State.NORMAL)
			):
				print_handler("Thread - Acceleration", f"{self.state} -> {self.transition_state}")
				self.state = self.transition_state

		# When the algorithm transitions from its CLIMAX state to its INVERSE state, a crash has occurred
		if self.state == State.INVERSE and self.transition == transition_threshold:
			return True
		else:
			return False

	def export_data(self, directory):
		"""
		Save the last x seconds of acceleration data to its own csv file
		"""
		try:
			output_directory = directory.get()
			output_file_name = '/accelerometer_' + time.strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
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

class State(Enum):
	NORMAL = "normal"
	CLIMAX = "climax"
	INVERSE = "inverse"