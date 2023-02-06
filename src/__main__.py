from threading import Event, Thread
import os
import RPi.GPIO as GPIO
from print_handler import print_handler
import accelerometer_thread
import camera_thread
import capture_thread
import ultrasonic_thread

""" Poweron sequence """
POWER_STATUS_LED = 20
POWER_OFF_BUTTON = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_STATUS_LED, GPIO.OUT)
GPIO.setup(POWER_OFF_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(POWER_STATUS_LED, True)
print_handler("Main", "Program started")

""" Events """
poweroff_event = Event()
crash_event = Event()
a_capture_event = Event()
c_capture_event = Event()
u_capture_event = Event()

""" Threads """
threads = [
	Thread(target=accelerometer_thread.Start, args=[poweroff_event, crash_event, a_capture_event]),
	Thread(target=camera_thread.Start, args=[poweroff_event, c_capture_event]),
	Thread(target=capture_thread.Start, args=[poweroff_event, crash_event, a_capture_event, c_capture_event, u_capture_event]),
	Thread(target=ultrasonic_thread.Start, args=[poweroff_event, u_capture_event]),
]
[ thread.start() for thread in threads ]

""" Poweroff sequence """
GPIO.wait_for_edge(POWER_OFF_BUTTON, edge=GPIO.FALLING)
poweroff_event.set()
[ thread.join() for thread in threads ]
GPIO.output(POWER_STATUS_LED, False)
GPIO.cleanup(POWER_STATUS_LED)
GPIO.cleanup(POWER_OFF_BUTTON)
print_handler("Main", "Program stopped")
os.system("sudo poweroff")