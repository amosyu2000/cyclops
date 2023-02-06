import video_capture
from time import sleep
import threading

output_directory = '/home/capstone/Documents/recording/output_files/'
temp_directory ='/home/capstone/Documents/recording/temporary_files/'

video_length        = 15
num_partitions      = 2
frames_per_second   = 30
camera_number       = -1
resolution          = 0
app = video_capture.Buffer(video_length, num_partitions, frames_per_second, output_directory, temp_directory, camera_number, resolution)
buffer = threading.Thread(name='start_buffer', target=app.start_buffer)
buffer.start()

#-------------------------------------------------

# live demo: c -> clip, s -> stop

sleep(20)
app.log_buffer()


#-------------------------------------------------

# test case 1: baseline
#sleep(video_length+2)
#app.log_buffer()

#-------------------------------------------------  

# test case 2: early clip
#sleep(video_length/2)
#app.log_buffer()

#-------------------------------------------------

# test case 3: spam clip
#sleep(video_length/2)
#app.log_buffer()
#app.log_buffer()
#sleep(video_length/5)
#app.log_buffer()

#-------------------------------------------------

# used in all test cases
app.stop_buffer()

