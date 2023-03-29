import serial, time, numpy, queue
from dir_handler import Dir_Handler
from print_handler import print_handler

class Lidar():
	def __init__(self, sample_rate:int, baud_rate:int):
		"""
		@sample_rate: [1-250] Number of distance sensor readings per second.
		"""
		self.lidar_serial = serial.Serial("/dev/serial0", baud_rate,timeout=0) # mini UART serial device
		if not self.lidar_serial.isOpen():
			self.lidar_serial.open() # open serial port if not open
		self.set_sample_rate(sample_rate)
		self.lidar_data = queue.Queue(60*sample_rate) # retain the last 60 econds of data
		self.dir_handler = Dir_Handler() # provides name of a dynamic output directory

	def set_sample_rate(self, sample_rate:int):
		"""
		Change the number of distance sensor readings per second.

		@sample_rate: [1-250]
		"""
		self.lidar_serial.write([0x5a, 0x06, 0x03, sample_rate, 00, 00]) # send sample rate instruction

	def read_data(self):
		"""
		Returns the distance of an object in cm
		"""
		while (self.lidar_serial.in_waiting < 9):
			time.sleep(0.01)
		raw_lidar_data = self.lidar_serial.read(9)
		self.lidar_serial.reset_input_buffer()
		if raw_lidar_data[0]!=0x59 or raw_lidar_data[1]!=0x59: # validate the data using first 2 bytes
			print_handler("Thread - Lidar", "Invalid Data")
			return None
		distance = (raw_lidar_data[2] + raw_lidar_data[3]*256)
		signal_strength = raw_lidar_data[4] + raw_lidar_data[5]*256
		temperature = raw_lidar_data[6]/8.0 + raw_lidar_data[7]*32.0 - 256

		if self.lidar_data.full():
			self.lidar_data.get()
		self.lidar_data.put([time.time(), distance, signal_strength, temperature])
		return distance
		
	def export_data(self):
		try:
			output_directory = self.dir_handler.locate_export_dir('lidar')
			output_file_name = '/lidar_' + time.strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
			with open(output_directory + output_file_name, 'w') as csv_file:
				csv_file.write('Time, Distance, Signal Stength, Temperature\n')
				while not self.lidar_data.empty():
					csv_file.write(str(self.lidar_data.get())[1:-1] + '\n')
			csv_file.close
		except:
			print_handler("Thread - Lidar", "An error occured while saving the data at: " + output_directory + output_file_name)
		else:
			print_handler("Thread - Lidar", "Saved last 60 seconds of data to: " + output_directory + output_file_name)

	def close(self):
		if self.lidar_serial.isOpen():
			self.lidar_serial.close() # open serial port if not open