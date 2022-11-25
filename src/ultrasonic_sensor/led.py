import math
import RPi.GPIO as GPIO

class LED:
	def __init__(self, *pins):
		self.pins = pins
		self.partitions = len(self.pins)
		GPIO.setmode(GPIO.BCM)
		[ GPIO.setup(pin, GPIO.OUT) for pin in self.pins ]

	def percentage_high(self, percent):
		max_i = math.floor(percent * self.partitions)
		print("LED output set to (", end="")
		for i in range(self.partitions):
			if (i <= max_i):
				GPIO.output(self.pins[i], GPIO.HIGH)
				print("1", end="")
			else:
				GPIO.output(self.pins[i], GPIO.LOW)
				print("0", end="")
		print(")")

	def cleanup(self):
		GPIO.cleanup()
