from threading import Event, Thread
from gpiozero import Button
import os
import RPi.GPIO as GPIO
from print_handler import print_handler
import accelerometer.start as Accelerometer
import ultrasonic_sensor.start as Ultrasonic
import recording.start as Recording

""" Poweron sequence """
GPIO.setmode(GPIO.BCM)
POWER_STATUS_LED = 20
GPIO.setup(POWER_STATUS_LED, GPIO.OUT)
GPIO.output(POWER_STATUS_LED, True)
print_handler("Main", "Program started")

""" Events """
poweroff_event = Event()

""" Threads """
threads = [
	Thread(target=Accelerometer.Start, args=[poweroff_event]),
	Thread(target=Ultrasonic.Start, args=[poweroff_event]),
	# Thread(target=lambda: Recording.Start(isCrashed)),
]
[ thread.start() for thread in threads ]

""" Poweroff sequence """
Button(21).wait_for_press()
poweroff_event.set()
[ thread.join() for thread in threads ]
GPIO.output(POWER_STATUS_LED, False)
GPIO.cleanup(POWER_STATUS_LED)
print_handler("Main", "Program stopped")
# os.system("sudo poweroff")