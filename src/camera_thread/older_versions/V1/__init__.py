import threading
from threading import Event
from camera_thread.video_capture import Buffer
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event, capture_event):
		print_handler("Thread", "Video Capture thread started")

		video_length        = 60
		num_partitions      = 3
		frames_per_second   = 24
		temp_directory      = '/home/capstone/Documents/temp/video/'
		camera_number       = -1
		resolution          = 1
		
		cap = Buffer(video_length, num_partitions, frames_per_second, temp_directory, camera_number, resolution)
		grab= threading.Thread(name='grab_frames', target=cap.grab_frames)
		grab.start()
		log = threading.Thread(name='log_frames', target=cap.log_frames)
		log.start()
		while not poweroff_event.is_set():
			if capture_event.is_set():
				cap.log_buffer()
				capture_event.clear()
		cap.stop_buffer()

if __name__ == '__main__':
	Start(Event(), Event())