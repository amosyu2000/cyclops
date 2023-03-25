from threading import Event, Thread
import time
from camera_thread.video_capture import Threaded_Video_Writing
from print_handler import print_handler

class Start:
	def __init__(self, poweroff_event, capture_event):
		
		video_length = 60 # min length of video captures in seconds
		fps = 30

		max_frames = video_length * fps
		frame_counter = 0
		video_writer = Threaded_Video_Writing(fps)

		print_handler("Thread - Camera", "Video Camera thread started")

		loop_time = float(1/fps)
		while not poweroff_event.is_set():
			start_time = time.time()
			if not capture_event.is_set():
				video_writer.write_frame()
				frame_counter += 1
				if frame_counter == max_frames:
					video_writer.refresh()
					frame_counter = 0
				else:
					sleep_time = loop_time - (time.time()-start_time) - .0005 # the final term is a tuning parameter
					if sleep_time > 0:
						time.sleep(sleep_time)
			else:
				video_writer.log_video()
				capture_event.clear()
		
		video_writer.close()
		print_handler("Thread - Camera", "Video Camera thread safely stopped")

if __name__ == '__main__':
	Start(Event(), Event())