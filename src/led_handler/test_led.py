import board, neopixel, time

class Led_Handler:
	def __init__(self):
		"""
		Utility class for displaying different light patterns on the  Adafruit NeoPixel Stick
		"""
		pixel_pin = board.D18
		self.num_pixels = 8
		self.pixels = neopixel.NeoPixel(pixel_pin, self.num_pixels, brightness=0.3, auto_write=False)
		
		self.color_gradient = [[255, 0, 0], [252, 64, 0], [249, 128, 0], [245, 191, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0]]

	def startup_sequence(self):
		"""
		Displays an LED sequence to acknowledge power on
		"""
		self.pixels.fill((0, 0, 0))

		# PUT PIXEL ANIMATION HERE
		for i in range(self.num_pixels):
			self.pixels[i] = (0, 255, 0)
			self.pixels.show()
			time.sleep(0.2)

		brightness_change = -1
		current_brightness = 255
		for i in range(6):
			for j in range(250):
				current_brightness += brightness_change
				self.pixels.fill((0, current_brightness, 0))
				self.pixels.show()
				time.sleep(0.001)
			brightness_change *= -1

		self.pixels.fill((0, 0, 0))
		print("Startup sequence displayed!")
	
	def poweroff_sequence(self):
		"""
		Displays an LED sequence to acknowledge power off
		"""
		self.pixels.fill((255, 0, 0))

		# PUT PIXEL ANIMATION HERE

		brightness_change = -1
		current_brightness = 255
		for i in range(6):
			for j in range(250):
				current_brightness += brightness_change
				self.pixels.fill((current_brightness, 0, 0))
				self.pixels.show()
				time.sleep(0.001)
			brightness_change *= -1

		for i in range(self.num_pixels):
			self.pixels[i] = (0, 0, 0)
			self.pixels.show()
			time.sleep(0.2)

		self.pixels.fill((0, 0, 0))
		print("poweroff sequence displayed!")

	def capture_sequence(self):
		"""
		Displays an LED sequence to acknowledge a capture event
		"""
		self.pixels.fill((0, 0, 0))

		# PUT PIXEL ANIMATION HERE
		for i in range(5):
			self.pixels.fill((0, 0, 255))
			self.pixels.show()
			time.sleep(0.2)
			self.pixels.fill((0, 0, 0))
			self.pixels.show()
			time.sleep(0.2)

		self.pixels.fill((0, 0, 0))
		print("capture sequence displayed!")

	def distance_display(self, led_arr):
		"""
		Displays an led equivalent of the distance detected

		@led_arr: an array of 8 single bits dictating the state of each led (on/off)
		"""
		# PUT IT HERE
		for i in range(8):
			if led_arr[i]:
				self.pixels[i] = (self.color_gradient[i])
			else:
				self.pixels[i] = ((0, 0, 0))
		self.pixels.show()
		
led = Led_Handler()
led.startup_sequence()
time.sleep(1)
led.capture_sequence()
time.sleep(1)
led.poweroff_sequence()