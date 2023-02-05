import csv
import io
import os
import pandas
import time
from dir_handler import Dir_Handler
from print_handler import print_handler

class CSV_Handler:
	def __init__(self, filename):
		"""
		Utility class for handling all actions related to csv files
		Remember to run open() before anything, and close() when you're done

		@filename: File name of the csv file, location is defined by the CSV_Handler class
		"""

		self.filename = filename
		self.temp_dir = "/home/capstone/Documents/temp"
		self.temp_filepath = f"{self.temp_dir}/{self.filename}_{time.strftime('%Y-%m-%d_%H:%M:%S')}.csv"
		self.dir_handler = Dir_Handler()
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

		@data_array: list of values that will become a comma-separated line in the csv file
		"""

		if self.file_is_open():
			self.csv_writer.writerow([ time.time() ] + data_array)

	def export_latest(self, seconds):
		"""
		Save some data from the temporary csv to a more permanent file whose location is handled by Dir_Handler 

		@seconds: The amount of time, in seconds, of past data to save
		"""

		# Temporarily close and reopen the file so that we can read the data from it
		self.close()
		df = pandas.read_csv(self.temp_filepath, header=None)
		self.open()

		current_time = time.time()
		export_df = df[df[0].between(current_time-seconds, current_time)]
		output_filepath = f"{self.dir_handler.locate_export_dir(self.filename)}/{self.filename}_{time.strftime('%Y-%m-%d_%H:%M:%S')}.csv"
		export_df.to_csv(output_filepath, index=False, header=False)

		print_handler("CSV", f"Saved last {seconds} seconds of data to \"{output_filepath}\".")

	def close(self):
		if self.file_is_open():
			self.file.close()
