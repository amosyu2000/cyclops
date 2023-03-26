import RPi.GPIO as GPIO
import time
from threading import Event
from print_handler import print_handler
from led_handler import Led_Handler

class Start:
	def __init__(self, poweroff_event, log_event, *thread_capture_events):
		print_handler("Thread - Capture", "Capture thread started")

		self.log_event = log_event
		self.PIN_CAPTURE = 21
		self.thread_capture_events = thread_capture_events
		self.led_handler = Led_Handler()

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.PIN_CAPTURE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.add_event_detect(self.PIN_CAPTURE, edge=GPIO.FALLING, callback=self.capture_button_pushed, bouncetime=3000)

		while not poweroff_event.is_set():
			if self.log_event.is_set():
				self.set_capture_events()
				start_time = time.time()
				graceful_exit = True
				while self.is_set(): # verify that all thread_capture_events are lowered
					if time.time()-start_time>6:
						graceful_exit = False
						break
					time.sleep(0.1)
				if graceful_exit:
					print_handler("Thread - Capture", "Capture sucessful")
					self.led_handler.capture_sequence()
				else:
					debug = self.event_status()
					print_handler("Thread - Capture", "Capture failed, alotted time has expired. \n[Accelerometer, Camera, LiDar] \nEvent Status: " + str(debug) + "\nExpected: [False, False, False]")
					self.led_handler.error_capture_sequence(debug)
				self.log_event.clear()
			time.sleep(0.1)

		self.close()
		print_handler("Thread - Capture", "Capture thread safely stopped")

	def capture_button_pushed(self, pin):
		print_handler("Thread - Capture", f"Button {pin} pushed")
		self.log_event.set()
	
	def set_capture_events(self):
		for event in self.thread_capture_events:
			event.set()

	def is_set(self):
		for event in self.thread_capture_events:
			if event.is_set(): return True
		return False
	
	def event_status(self):
		out = []
		for event in self.thread_capture_events:
			out.append(event.is_set())
		return out

	def close(self):
		GPIO.remove_event_detect(self.PIN_CAPTURE)
		GPIO.cleanup(self.PIN_CAPTURE)

if __name__ == '__main__':
	Start(Event(), Event())