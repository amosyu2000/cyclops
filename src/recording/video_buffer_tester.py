import video_buffer
from time import sleep
import threading

def __main__():
    pi_output_dir = '/home/capstone/Documents/start_camera_buffer/output_files/'
    manny_output_dir = '/Users/mannylemos/Desktop/4TB6 - Capstone/low_ram_split/output_files/'

    pi_temp_dir = '/home/capstone/Documents/start_camera_buffer/temporary_files/'
    manny_temp_dir = '/Users/mannylemos/Desktop/4TB6 - Capstone/low_ram_split/temporary_files/'
    
    video_length        = 10
    num_partitions      = 3
    frames_per_second   = 30
    output_directory    = pi_output_dir
    temp_directory      = pi_temp_dir
    camera_number       = 0
    resolution          = 0
    
    app = video_buffer.Buffer(video_length, num_partitions, frames_per_second, output_directory, temp_directory, camera_number, 1)
    buffer = threading.Thread(name='start_buffer', target=app.start_buffer)
    buffer.start()

    #-------------------------------------------------

    # test case 1: baseline
    sleep(video_length+2)
    app.log_buffer()
    
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

__main__()