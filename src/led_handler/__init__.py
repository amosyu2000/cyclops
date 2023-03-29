import board, neopixel, time

class Led_Handler:
	def __init__(self, log_event):
		"""
		Utility class for displaying different light patterns on the  Adafruit NeoPixel Stick
		"""
		pixel_pin = board.D18
		self.num_pixels = 8
		self.pixels = neopixel.NeoPixel(pixel_pin, self.num_pixels, brightness=0.3, auto_write=False)
		self.log_event = log_event

		self.red = (100, 0, 0)
		self.bright_red = (150, 0, 0)
		self.blue = (0, 0, 100)
		self.bright_blue = (0, 0, 150)
		self.off = (0, 0, 0)
		# R -> G
		# self.color_gradient = [[255, 0, 0], [252, 64, 0], [249, 128, 0], [245, 191, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0]] 

		# G -> R
		self.color_gradient = [[0, 100, 0], [33, 100, 0], [66, 100, 0], [100, 100, 0], [96, 74, 0], [97, 50, 0], [98, 25, 0], [100, 0, 0]]

	def startup_sequence(self):
		"""
		Displays an LED sequence to acknowledge power on
		"""
		self.pixels.fill(self.off)

		# PIXEL ANIMATION
		for i in range(self.num_pixels):
			self.pixels[i] = (0, 100, 0)
			self.pixels.show()
			time.sleep(0.2)

		brightness_change = -1
		current_brightness = 100
		for i in range(6):
			for j in range(100):
				current_brightness += brightness_change
				self.pixels.fill((0, current_brightness, 0))
				self.pixels.show()
				time.sleep(0.002)
			brightness_change *= -1

		self.pixels.fill(self.off)
		self.pixels.show()
	
	def poweroff_sequence(self):
		"""
		Displays an LED sequence to acknowledge power off
		"""
		self.pixels.fill((100, 0, 0))

		# PIXEL ANIMATION

		brightness_change = -1
		current_brightness = 100
		for i in range(6):
			for j in range(100):
				current_brightness += brightness_change
				self.pixels.fill((current_brightness, 0, 0))
				self.pixels.show()
				time.sleep(0.002)
			brightness_change *= -1

		for i in range(self.num_pixels):
			self.pixels[i] = self.off
			self.pixels.show()
			time.sleep(0.2)

		self.pixels.fill(self.off)
		self.pixels.show()

	def capture_sequence(self, debug):
		self.pixels.fill(self.off)
		reg_fill_colour = [self.red] * 3
		bright_fill_colour = [self.bright_red] * 3

		# PIXEL ANIMATION
		for i, state in enumerate(debug):
			if not state:
				reg_fill_colour[i] = self.blue
				bright_fill_colour[i] = self.bright_blue
		
		for i in range(5):
			self.pixels[0:len(reg_fill_colour)] = reg_fill_colour
			self.pixels.show()
			time.sleep(0.3)
			self.pixels[0:len(reg_fill_colour)] = [self.off] * len(reg_fill_colour)
			self.pixels.show()
			time.sleep(0.3)


	def distance_display(self, distance):
		"""
		Displays an led equivalent of the distance detected

		@distance: distance of objects in cm
		"""
		leds_on = 8 - distance // 100
		lower_bound = 0
		if self.log_event.is_set():
			lower_bound = 3
		self.pixels[lower_bound: 8] = [self.off]*(8-lower_bound)
		for i in range(lower_bound, leds_on):
			self.pixels[i] = (self.color_gradient[i])
		self.pixels.show()