import cv2
import ffmpeg
import threading
import time
import os

# TESTING LINE
from datetime import datetime

class Buffer:
	def __init__(self, video_length:int, num_partitions:int, fps:int, save_directory:str, temp_directory:str, camera_id:int, resolution:int):

		"""
		Write and overwrite sequential recordings such that a minimum of video_length time 
		of recorded material is available to be logged at any given time.

		@video_length: The length in seconds of the requested video.
		@num_partitions: [2->10] more partitions = higher concatenation time and lower storage usage
		@fps: Number of frames requested from camera every second.
		@save_Directory: The full directory you wish to save recordings at
		@temp_Directory: The full directory used to temporarily store .mp4 clips
		@camera_id: -1 -> Automatically detect camera, >=0 -> Manually identify by webcam index
		@resolution: -1 -> Automatically detect resolution, 0 -> 640x480, 1 ->  1280x720, 2 -> 1920x1080
		"""

		self.video_length = video_length
		self.output_directory = save_directory
		self.temp_directory = temp_directory
		self.camera_id = camera_id
		self.cap = cv2.VideoCapture(self.camera_id) # create a capture object
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

	def stop_buffer(self):
		self.lock.acquire()
		self.run_buffer = False
		self.lock.release()

	def log_buffer(self):
		self.lock.acquire()  
		
		startTime = datetime.now() # TESTING LINE

		# release the current result video, this allows it to be accessed
		self.result.release()
		output_file_name = time.strftime("%Y_%m_%d-%I_%M_%S_%p") +'.mp4'

		# trim the oldest video to achieve a concatenated video time == self.video_length
		idx = (self.vid_num+1)%self.num_partitions
		if os.path.isfile(self.temp_directory + str(idx) + ".mp4"):
			(
				ffmpeg
				.input(self.temp_directory + str(idx) + ".mp4")
				.trim(start_frame = self.curr_frames, end_frame = self.max_frames)
				.setpts ('PTS-STARTPTS') # sets start time to start frame
				.output (self.temp_directory + str(idx) + "_.mp4", loglevel="quiet")
				.run(overwrite_output=True)
			) # rename the file to the expected naming pattern (#.mp4)
			os.rename(self.temp_directory + str(idx) + "_.mp4", self.temp_directory + str(idx) + ".mp4")

		# store videos as ffmpeg.input objects in an array chronologically
		file_arr = []
		for i in range(self.vid_num+1, self.num_partitions):
			if os.path.isfile(self.temp_directory + str(i) + ".mp4"):
				file_arr.append(ffmpeg.input(self.temp_directory + str(i) + ".mp4"))
		for i in range(0, self.vid_num+1):
			if os.path.isfile(self.temp_directory + str(i) + ".mp4"):
				file_arr.append(ffmpeg.input(self.temp_directory + str(i) + ".mp4"))
		# concatanate files & rename the output
		(
			ffmpeg
			.concat(*file_arr)
			.output(self.output_directory + output_file_name, loglevel="quiet")
			.run(overwrite_output=True)
		)
		# delete unused files
		for i in range(0, len(file_arr)):
			os.remove(self.temp_directory + str(i) + ".mp4")
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

	def start_buffer(self):
		# Implementation:
		# sequentially write clips with number_frames = self.fps * self.video_length = self.max_frames
		# clips are named 0.mp4, 1.mp4, ... , str(self.num_partitions-1).mp4
		# once self.num_partitions clips have been written, begin overwritting 0.mp4 as this footage is beyond self.video_length

		while(self.run_buffer):
			self.lock.acquire()
			ret, frame = self.cap.read() # get most recent from from cap

			if self.curr_frames < self.max_frames:
				# continue current video
				self.curr_frames += 1
				self.result.write(frame)
			else:
				# save current video (overwriting old video if one exists), start a new video
				self.curr_frames = 0
				self.result.release()
				self.vid_num = (self.vid_num+1)%(self.num_partitions)
				self.result = cv2.VideoWriter(  self.temp_directory + str(self.vid_num) + ".mp4", 		# save directory + file name
												cv2.VideoWriter_fourcc('m', 'p', '4', 'v'),					# use mp4v codec
												self.fps, 													# fps
												(self.frame_width, self.frame_height))						# frame size

			# release the lock before the end of the while loop to allow other
			# pieces of the code to grab the mutex  
			self.lock.release()
			time.sleep(0.0001)

		# exit sequence
		# release cap & destroy cv2 windows -> then exit
		self.cap.release()
		cv2.destroyAllWindows()