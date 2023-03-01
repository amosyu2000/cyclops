import math
import RPi.GPIO as GPIO
from print_handler import print_handler

class LED:
	def __init__(self, *pins):
		"""
		Initialize the GPIO pins for the row of LED lights

		@*pins: List of the pin numbers to initialize
		"""
		self.pins = pins
		self.partitions = len(self.pins)
		GPIO.setmode(GPIO.BCM)
		[ GPIO.setup(pin, GPIO.OUT) for pin in self.pins ]

	def percentage_high(self, percent):
		"""
		Turn a percentage of the row of LED lights on

		@percent: Percentage of lights to turn on (ex. 0.65 of five lights will turn on three lights)
		"""
		max_i = math.floor(percent * self.partitions)
		print_output = ""
		for i in range(self.partitions):
			if (i <= max_i):
				GPIO.output(self.pins[i], GPIO.HIGH)
				print_output += "1"
			else:
				GPIO.output(self.pins[i], GPIO.LOW)
				print_output += "0"
		#print_handler("LED", f"Output set to {print_output}")

	def close(self):
		[ GPIO.cleanup(pin) for pin in self.pins ]
