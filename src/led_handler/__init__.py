import board, neopixel, time

class Led_Handler:
	def __init__(self):
		"""
		Utility class for displaying different light patterns on the  Adafruit NeoPixel Stick
		"""
		pixel_pin = board.D18
		self.num_pixels = 8
		self.pixels = neopixel.NeoPixel(pixel_pin, self.num_pixels, brightness=0.3, auto_write=False)
		
		# R -> G
		# self.color_gradient = [[255, 0, 0], [252, 64, 0], [249, 128, 0], [245, 191, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0]] 

		# G -> R
		self.color_gradient = [[0, 255, 0], [85, 255, 0], [170, 255, 0], [255, 255, 0], [245, 191, 0], [249, 128, 0], [252, 64, 0], [255, 0, 0]]

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

	def error_capture_sequence(self, debug):
		self.pixels.fill((0, 0, 0))
		fill_colour = [(255, 0 , 0), (255, 0 , 0), (255, 0 , 0), (255, 0 , 0), (255, 0 , 0), (255, 0 , 0), (255, 0 , 0), (255, 0 , 0)]

		# PUT PIXEL ANIMATION HERE
		if not debug[0]:
			fill_colour[0] = (0, 0, 255)
			fill_colour[1] = (0, 0, 255)
			fill_colour[2] = (0, 0, 255)
		if not debug[1]:
			fill_colour[3] = (0, 0, 255)
			fill_colour[4] = (0, 0, 255)
			fill_colour[5] = (0, 0, 255)
		if not debug[2]:
			fill_colour[6] = (0, 0, 255)
			fill_colour[7] = (0, 0, 255)
		
		for i in range(5):
			for j in range(8):
				self.pixels[j] = fill_colour[j]
			self.pixels.show()
			time.sleep(0.2)
			self.pixels.fill((0, 0, 0))
			self.pixels.show()
			time.sleep(0.2)


	def distance_display(self, distance):
		"""
		Displays an led equivalent of the distance detected

		@distance: distance of objects in cm
		"""
		leds_on = 8 - distance // 100
		self.pixels.fill((0, 0, 0))
		for i in range(leds_on):
			self.pixels[i] = (self.color_gradient[i])
		self.pixels.show()