import matplotlib.pyplot as plt
import numpy as np
from statistics import fmean

class Acceleration_Plot:
	def __init__(self, data_points, average_of=1):
		"""
		Create a matplotlib plot to display live acceleration data

		@data_points: Maximum number of data points to show on the plot
		@average_of: Takes a rolling average of the xyz acceleration points
		"""
		
		self.data_points = data_points
		self.average_of = average_of

		self.raw_x = [0] * self.average_of
		self.raw_y = [0] * self.average_of
		self.raw_z = [0] * self.average_of
		self.raw_norm = [0] * self.average_of
		self.avg_x = []
		self.avg_y = []
		self.avg_z = []
		self.avg_norm = []
		self.t = []

		self.plt_xline, = plt.plot(self.t, self.avg_x, 'r', label="x")
		self.plt_yline, = plt.plot(self.t, self.avg_y, 'b', label="y")
		self.plt_zline, = plt.plot(self.t, self.avg_z, 'g', label="z")
		self.plt_normline, = plt.plot(self.t, self.avg_norm, 'k', label="norm")
		self.plt_ax = plt.gca()

		plt.legend(loc="upper left")
		plt.title("Live accelerometer data")
		plt.xlabel("Time")
		plt.ylabel("Acceleration (m/s^2)")

	def update(self, x, y, z, t):
		"""
		Add a new set of acceleration data to the plot

		@x: x component of acceleration
		@y: y component of acceleration
		@z: z component of acceleration
		@t: time
		"""

		self.raw_x.append(x)
		self.raw_y.append(y)
		self.raw_z.append(z)
		self.raw_norm.append(np.linalg.norm([x,y,z]))

		self.raw_x.pop(0)
		self.raw_y.pop(0)
		self.raw_z.pop(0)
		self.raw_norm.pop(0)

		self.avg_x.append(fmean(self.raw_x))
		self.avg_y.append(fmean(self.raw_y))
		self.avg_z.append(fmean(self.raw_z))
		self.avg_norm.append(fmean(self.raw_norm))
		self.t.append(t)

		if len(self.t) > self.data_points:
			self.avg_x.pop(0)
			self.avg_y.pop(0)
			self.avg_z.pop(0)
			self.avg_norm.pop(0)
			self.t.pop(0)

		self.plt_xline.set_data(self.t, self.avg_x)
		self.plt_yline.set_data(self.t, self.avg_y)
		self.plt_zline.set_data(self.t, self.avg_z)
		self.plt_normline.set_data(self.t, self.avg_norm)
		self.plt_ax.relim()
		self.plt_ax.autoscale_view()

	def pause(self, seconds):
		"""
		Pause the plot for an amount of time

		@seconds: Time to pause the plot for, in seconds
		"""

		plt.pause(seconds)
