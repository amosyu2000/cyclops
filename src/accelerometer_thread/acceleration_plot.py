import matplotlib.pyplot as plt
import time
from accelerometer_thread import Acceleration
from print_handler import print_handler

class Acceleration_Plot:
	def __init__(self, acceleration, data_points):
		"""
		Create a matplotlib plot to display live acceleration data

		@acceleration: An Acceleration object
		@data_points: Maximum number of data points to show on the plot
		"""

		self.acceleration = acceleration
		self.data_points = data_points

		self.points_x = []
		self.points_y = []
		self.points_z = []
		self.points_norm = []
		self.points_t = []

		self.plt_xline, = plt.plot(self.points_t, self.points_x, 'r', label="x")
		self.plt_yline, = plt.plot(self.points_t, self.points_y, 'b', label="y")
		self.plt_zline, = plt.plot(self.points_t, self.points_z, 'g', label="z")
		self.plt_normline, = plt.plot(self.points_t, self.points_norm, 'k', label="norm")
		self.plt_ax = plt.gca()

		plt.legend(loc="upper left")
		plt.title("Live accelerometer data")
		plt.xlabel("Time")
		plt.ylabel("Acceleration (m/s^2)")

	def update(self):
		"""
		Update the plot with new acceleration data
		"""

		self.acceleration.temp_log()

		self.points_x.append(self.acceleration.get_avg_x())
		self.points_y.append(self.acceleration.get_avg_y())
		self.points_z.append(self.acceleration.get_avg_z())
		self.points_norm.append(self.acceleration.get_avg_norm())
		self.points_t.append(time.time())

		if len(self.points_t) > self.data_points:
			self.points_x.pop(0)
			self.points_y.pop(0)
			self.points_z.pop(0)
			self.points_norm.pop(0)
			self.points_t.pop(0)

		self.plt_xline.set_data(self.points_t, self.points_x)
		self.plt_yline.set_data(self.points_t, self.points_y)
		self.plt_zline.set_data(self.points_t, self.points_z)
		self.plt_normline.set_data(self.points_t, self.points_norm)
		self.plt_ax.relim()
		self.plt_ax.autoscale_view()

		# print_handler("Acceleration_Plot", "Updated plot")

	def pause(self, seconds):
		"""
		Pause the plot for an amount of time

		@seconds: Time to pause the plot for, in seconds
		"""

		plt.pause(seconds)

	def close(self):
		"""
		Close the plot and the log file
		"""

		plt.close()
		self.acceleration.close()
