from threading import Event, Thread
import os
import RPi.GPIO as GPIO
from print_handler import print_handler
from led_handler import Led_Handler
import accelerometer_thread, camera_thread, lidar_thread, capture_thread

""" Events """
poweroff_event = Event()
log_event = Event()
a_capture_event = Event()
c_capture_event = Event()
l_capture_event = Event()

""" Poweron sequence """
POWER_OFF_BUTTON = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(POWER_OFF_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_handler = Led_Handler(log_event)
led_handler.startup_sequence()
print_handler("Main", "Program started")

""" Threads """
threads = [
	Thread(target=accelerometer_thread.Start, args=[poweroff_event, log_event, a_capture_event]),
	Thread(target=camera_thread.Start, args=[poweroff_event, c_capture_event]),
	Thread(target=lidar_thread.Start, args=[poweroff_event, l_capture_event, led_handler]),
	Thread(target=capture_thread.Start, args=[led_handler, poweroff_event, log_event, a_capture_event, c_capture_event, l_capture_event]),
]
[ thread.start() for thread in threads ]

""" Poweroff sequence """
GPIO.wait_for_edge(POWER_OFF_BUTTON, edge=GPIO.FALLING)
poweroff_event.set()
[ thread.join() for thread in threads ]

led_handler.poweroff_sequence()
GPIO.cleanup(POWER_OFF_BUTTON)
print_handler("Main", "Program stopped")
os.system("sudo poweroff")