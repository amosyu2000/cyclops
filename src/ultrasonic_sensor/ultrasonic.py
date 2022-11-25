import RPi.GPIO as GPIO
import time

class Ultrasonic:
	def __init__(self, pin_trigger, pin_echo, distance_min, distance_max, unit):
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
		return (self.distance_max - self.distance_absolute()) / (self.distance_max - self.distance_min)

	def cleanup(self):
		GPIO.cleanup()
