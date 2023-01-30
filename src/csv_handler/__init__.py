import csv
import io
import os
import pandas
import time

class CSV_Handler:
	def __init__(self, filename):
		"""
		Utility class for handling all actions related to csv files
		Remember to run open() before anything, and close() when you're done

		@filename: File name of the csv file, location is defined by the CSV_Handler class
		"""

		self.output_dir = "/home/capstone/Documents"
		self.temp_dir = "/home/capstone/Documents/temp"
		self.output_filepath = f"{self.output_dir}/{filename}"
		self.temp_filepath = f"{self.temp_dir}/{filename}"
		self.file = None
		self.csv_writer = None
		
	def open(self):
		os.makedirs(os.path.dirname(self.temp_filepath), exist_ok=True)
		self.file = open(self.temp_filepath, "a+")
		self.csv_writer = csv.writer(self.file)

	def file_is_open(self):
		if isinstance(self.file, io.IOBase):
			return True
		raise Exception(f"File {self.temp_filepath} is not open")

	def writerow(self, data_array):
		"""
		Write a new row of values to the open csv file
		"""

		if self.file_is_open():
			self.csv_writer.writerow([ time.time() ] + data_array)

	def export_latest(self, seconds):
		"""
		Save the last x seconds of data from the csv
		"""

		# Temporarily close and reopen the file so that we can read the data from it
		self.close()
		df = pandas.read_csv(self.temp_filepath, header=None)
		self.open()

		current_time = time.time()
		export_df = df[df[0].between(current_time-seconds, current_time)]
		os.makedirs(os.path.dirname(self.output_filepath), exist_ok=True)
		export_df.to_csv(self.output_filepath, index=False, header=False)

	def close(self):
		if self.file_is_open():
			self.file.close()
