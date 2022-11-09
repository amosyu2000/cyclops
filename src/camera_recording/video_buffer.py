"""
PARAMETER           |   DATATYPE    |	Explanation   
--------------------|---------------|------------------------------------------------------
video_length        :   integer		:	The length in seconds of the video buffer
--------------------:---------------:------------------------------------------------------
frames_per_second   :	double		:	Number of frames requested from camera every second
--------------------:---------------:------------------------------------------------------
save_directory      :   string		:	The full directory you wish to save recordings at
--------------------:---------------:------------------------------------------------------
camera_number		:	integer		:	value		Explanation
										-1			Automatically detect camera
										>=0			Manually identify the webcam 
--------------------:---------------:------------------------------------------------------
resolution          :   integer		:	value		resolution		Explanation
										<=0		-> 	detect		-> 	N/A
										==1 	-> 	640x480		-> 	(low resolution)
										==2		-> 	1280x720	-> 	(medium resolution)
										>=3		-> 	1920x1080	-> 	(high resolution)
"""

import cv2
import threading
import time

# testing purposes only
from datetime import datetime

class Buffer:
	def __init__(self, video_length, frames_per_second, save_directory, camera_number, resolution):
		# class attributes
		self.buffer_time = video_length # length in seconds of video buffer
		self.output_directory = save_directory
		self.cam_slot = camera_number
		self.cap = cv2.VideoCapture(self.cam_slot)
		if resolution <= 0:
			self.frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			self.frame_height = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		elif resolution == 1:
			self.frame_width = 640
			self.frame_height = 480
		elif resolution == 2:
			self.frame_width = 1280
			self.frame_height = 720
		else:
			self.frame_width = 1920
			self.frame_height = 1080
			
		self.fps = frames_per_second
		self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
		self.cap.set(cv2.CAP_PROP_FPS, self.fps)
		
		self.buffer_index = 0 # the index of the frame_buffer that contains the oldest frame
		self.buffer_size = int(self.fps) * self.buffer_time
		self.frame_buffer = [None] * self.buffer_size 
		self.lock = threading.Lock() # mutex
		self.run_buffer = True

	def stop_buffer(self):
		self.lock.acquire()
		self.run_buffer = False
		self.lock.release()

	def log_buffer(self):
		self.lock.acquire()  
		
		# testing line
		startTime = datetime.now()
		
		output_file_name = time.strftime("%Y_%m_%d-%I_%M_%S_%p") +'.mp4'
		
		result = cv2.VideoWriter(   self.output_directory + output_file_name, 		# save directory + file name
									cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),		# use mp4v codec
									self.fps, 										# fps
									(self.frame_width, self.frame_height))			# frame size
			
		# write the frames to result
		for i in range(self.buffer_index, self.buffer_size):
			result.write(self.frame_buffer[i])
		for i in range(0, self.buffer_index):
			result.write(self.frame_buffer[i])

		# release the result & reset the capture instance
		result.release()
		self.cap.release()
		self.cap = cv2.VideoCapture(self.cam_slot)
		self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

		print("\n" + output_file_name + " was saved")
		self.frame_buffer = [None] * self.buffer_size # empty the frame buffer (prevents the same clips from being logged repeatedly)
		self.lock.release()
		
		print("logging runtime: " + str(datetime.now()-startTime) + " seconds")

	def start_buffer(self):
		while(self.run_buffer):
			self.lock.acquire()
			ret, frame = self.cap.read() # get most recent from from cap
			self.frame_buffer[self.buffer_index] = frame # store the frame in frame_buffer
			# release the lock before the end of the while loop to allow other
			# pieces of the code to grab the mutex  
			self.buffer_index = (self.buffer_index + 1) % self.buffer_size # increment buffer_index
			self.lock.release()
			time.sleep(0.0001)

		# release cap & destroy cv2 windows -> then exit
		self.cap.release()
		cv2.destroyAllWindows()