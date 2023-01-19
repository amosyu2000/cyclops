from recording.video_buffer import Buffer
import threading

def Start(isCrashed):
	if __name__ == '__main__':
		video_length        = 120
		num_partitions      = 10
		frames_per_second   = 30
		output_directory    = '/home/capstone/Documents/recording/output_files/'
		temp_directory      = '/home/capstone/Documents/recording/temporary_files/'
		camera_number       = -1
		resolution          = 0
		
		app = Buffer(video_length, num_partitions, frames_per_second, output_directory, temp_directory, camera_number, resolution)
		buffer = threading.Thread(name='start_buffer', target=app.start_buffer)
		buffer.start()

		while(True):
			if isCrashed:
				app.log_buffer()
				isCrashed = False