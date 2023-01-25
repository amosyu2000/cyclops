import RPi.GPIO as GPIO
import time
from ultrasonic_sensor.led import LED
from ultrasonic_sensor.ultrasonic import Ultrasonic

class Start():
	def __init__(self):
		led = LED(17, 22, 23, 25, 27)
		ultrasonic = Ultrasonic(pin_trigger=18, pin_echo=24, distance_min=0, distance_max=200, unit="cm")

		try:
			while True:
				led.percentage_high(ultrasonic.distance_percentage())
				time.sleep(0.5)
		# Reset by pressing CTRL + C
		except KeyboardInterrupt:
			print("Measurement stopped by User")
			GPIO.cleanup()


if __name__ == '__main__':
	Start()
