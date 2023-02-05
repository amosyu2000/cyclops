import RPi.GPIO as GPIO
import time
from threading import Event
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event, crash_event, *thread_capture_events):
		print_handler("Thread", "Capture thread started")

		self.PIN_CAPTURE = 21
		self.thread_capture_events = thread_capture_events

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.PIN_CAPTURE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.PIN_CAPTURE, edge=GPIO.FALLING, callback=self.capture_button_pushed, bouncetime=3000)

		while not poweroff_event.is_set():
			if crash_event.is_set():
				self.set_capture_events(None)
				crash_event.clear()
			time.sleep(0.1)

		self.close()
		print_handler("Thread", "Capture thread safely stopped")

	def capture_button_pushed(self, pin):
		print_handler("Capture", f"Button {pin} pushed")
		self.set_capture_events()
	
	def set_capture_events(self):
		for event in self.thread_capture_events:
			event.set()

	def close(self):
		GPIO.remove_event_detect(self.PIN_CAPTURE)
		GPIO.cleanup(self.PIN_CAPTURE)

if __name__ == '__main__':
	Start(Event(), Event())