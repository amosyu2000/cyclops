import RPi.GPIO as GPIO
import time

class Ultrasonic:
	def __init__(self, pin_trigger, pin_echo, distance_min, distance_max, unit):
		"""
		Initialize the GPIO pins for the ultrasonic sensor

		@pin_trigger: Pin number on the pi corresponding to the trigger pin on the sensor
		@pin_echo: Pin number on the pi corresponding to the echo pin on the sensor
		@distance_min: The closest distance that the ultrasonic sensor should detect
		@distance_max: The furthest distance that the ultrasonic sensor should detect
		@unit: Unit of the min and max distances (ex. cm)
		"""
		#set GPIO Pins
		self.PIN_TRIGGER = pin_trigger
		self.PIN_ECHO = pin_echo

		#GPIO Mode (BOARD / BCM)
		GPIO.setmode(GPIO.BCM)

		#set GPIO direction (IN / OUT)
		GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
		GPIO.setup(self.PIN_ECHO, GPIO.IN)

		self.distance_min = distance_min
		self.distance_max = distance_max
		self.unit = unit

	def distance_absolute(self):
		"""
		Get the absolute distance of an object in front of the sensor, in the unit specified
		"""
		# set Trigger to HIGH
		GPIO.output(self.PIN_TRIGGER, True)

		# set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.PIN_TRIGGER, False)

		StartTime = time.time()
		StopTime = time.time()

		# save StartTime
		while GPIO.input(self.PIN_ECHO) == 0:
			StartTime = time.time()

		# save time of arrival
		while GPIO.input(self.PIN_ECHO) == 1:
			StopTime = time.time()

		# time difference between start and arrival
		TimeElapsed = StopTime - StartTime

		if (self.unit == "cm"):
			distance_cm = (TimeElapsed * 34300) / 2
			print("Ultrasonic read distance of %.1fcm" % distance_cm)
			return distance_cm
	
	def distance_percentage(self):
		"""
		Get the distance of an object in front of the sensor as a percentage between the min and max distances
		"""
		return (self.distance_max - self.distance_absolute()) / (self.distance_max - self.distance_min)

	def cleanup(self):
		GPIO.cleanup()
