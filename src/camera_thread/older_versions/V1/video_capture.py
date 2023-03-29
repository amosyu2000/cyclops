import cv2
import ffmpeg
import threading
import time
import os
from print_handler import print_handler
from dir_handler import Dir_Handler

# TESTING LINE
from datetime import datetime

class Buffer:
	def __init__(self, video_length:int, num_partitions:int, fps:int, temp_directory:str, camera_id:int, resolution:int):

		"""
		Write and overwrite sequential recordings such that a minimum of video_length time 
		of recorded material is available to be logged at any given time.

		@video_length: The length in seconds of the requested video.
		@num_partitions: [2->10] The number of clips which will be combined to form the output video. As num_partitions increases; video concatenation time increases, disk storage decreases.
		@fps: Number of frames requested from camera every second.
		@save_Directory: The full directory you wish to save recordings at
		@temp_Directory: The full directory used to temporarily store .mp4 clips
		@camera_id: -1 -> Automatically detect camera, >=0 -> Manually identify by webcam index
		@resolution: -1 -> Automatically detect resolution, 0 -> 640x480, 1 ->  1280x720, 2 -> 1920x1080
		"""
		try: 
			self.video_length = video_length
			self.temp_directory = temp_directory
			for f in os.listdir(self.temp_directory):
				os.remove(os.path.join(self.temp_directory, f))
			self.camera_id = camera_id
			self.cap = cv2.VideoCapture(self.camera_id) # create a capture object

			# select resolution (auto, 480p, 720p, or 1080p)
			if resolution < 0: 
				self.frame_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
				self.frame_height = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
			elif resolution == 0:
				self.frame_width = 640
				self.frame_height = 480
			elif resolution == 1:
				self.frame_width = 1280
				self.frame_height = 720
			else:
				self.frame_width = 1920
				self.frame_height = 1080
				
			self.fps = fps

			# setting capture parameters
			self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG")) 
			self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
			self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)
			self.cap.set(cv2.CAP_PROP_FPS, self.fps)
			self.vid_num = 0
			self.result = cv2.VideoWriter(  self.temp_directory + str(self.vid_num) + ".mp4", # save location
											cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),			# use mp4v codec
											self.fps, 											# fps
											(self.frame_width, self.frame_height))				# frame size
			
			self.max_frames = int(self.fps) * self.video_length / (num_partitions-1)
			self.curr_frames = 0
			self.lock = threading.Lock() # mutex
			self.run_buffer = True
			self.num_partitions = num_partitions
			self.dir_handler = Dir_Handler() # provides name of a dynamic output directory (dictated by time of capture button push)
			self.frame = None
		except:
			print_handler("Error - video_capture.py", "Error during video initialization sequence. Check camera usb connection.")
	
	def stop_buffer(self):
		self.lock.acquire()
		self.run_buffer = False
		self.lock.release()

	def log_buffer(self):
		self.lock.acquire()  

		startTime = datetime.now() # TESTING LINE

		# release the current result video, this allows it to be accessed
		self.result.release()
		output_directory = self.dir_handler.locate_export_dir('video')
		output_file_name = '/video_' + time.strftime('%Y-%m-%d_%H-%M-%S') + '.mp4'

		# store videos names in txt file to be concatenated using ffmpeg demux
		f = open(self.temp_directory + "concat_list.txt", "w")
		num_files = 0
		for i in range(self.vid_num+1, self.num_partitions):
			if os.path.isfile(self.temp_directory + str(i) + ".mp4"):
				f.write("file '" + self.temp_directory + str(i) + ".mp4'\n")
				num_files += 1
		for i in range(0, self.vid_num+1):
			if os.path.isfile(self.temp_directory + str(i) + ".mp4"):
				f.write("file '" + self.temp_directory + str(i) + ".mp4'\n")
				num_files += 1
		f.close()
		try:
			if num_files > 1:
				# concatanate files & rename the output
				(
					ffmpeg
					.input(self.temp_directory + "concat_list.txt", format='concat', safe=0)
					.output(output_directory + output_file_name, loglevel="quiet", c='copy')
					.run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
				)
			else:
				os.rename(self.temp_directory + str(0) + ".mp4", output_directory + output_file_name)
		except:
			print_handler("Error - video_capture.py", "An error occured while concatenating or saving the output video at: "+output_directory + output_file_name)

		# delete files in temp directory
		for f in os.listdir(self.temp_directory):
			os.remove(os.path.join(self.temp_directory, f))
		# reset parameters
		self.curr_frames = 0
		self.vid_num = 0
		self.result = cv2.VideoWriter(  self.temp_directory + str(self.vid_num) + ".mp4", 	# save directory + file name
										cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),				# use mp4v codec
										self.fps, 												# fps
										(self.frame_width, self.frame_height))					# frame size
		print("\n" + output_file_name + " was saved")
		print("logging runtime: " + str(datetime.now()-startTime) + " seconds") # TESTING LINE
		self.lock.release()

	def grab_frames(self):
		while (self.run_buffer):
			ret, self.frame = self.cap.read() # get most recent from from cap

	def log_frames(self):
		# Implementation:
		# sequentially write clips with number_frames = self.fps * self.video_length = self.max_frames
		# clips are named 0.mp4, 1.mp4, ... , str(self.num_partitions-1).mp4
		# once self.num_partitions clips have been written, begin overwritting str(self.vid_num).mp4 
		# 	as this footage is beyond self.video_length

		while(self.run_buffer):
			self.lock.acquire()
			if self.curr_frames < self.max_frames:
				# continue current video
				self.curr_frames += 1
				self.result.write(self.frame)
			else:
				# save current video (overwriting old video if one exists), start a new video
				self.curr_frames = 0
				self.result.release()
				self.vid_num = (self.vid_num+1)%(self.num_partitions)
				self.result = cv2.VideoWriter(  self.temp_directory + str(self.vid_num) + ".mp4", 	# save directory + file name
												cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),			# use mp4v codec
												self.fps, 											# fps
												(self.frame_width, self.frame_height))				# frame size
				
			# release the lock before the end of the while loop to allow other
			# pieces of the code to grab the mutex  
			self.lock.release()

		# exit sequence
		# release cap & destroy cv2 windows -> then exit
		self.cap.release()
		cv2.destroyAllWindows()
