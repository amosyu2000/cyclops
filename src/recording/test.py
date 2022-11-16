import video_buffer
from time import sleep
import threading
import keyboard

def __main__():
    pi_output_dir = '/home/capstone/Documents/recording/output_files/'
    manny_output_dir = '/Users/mannylemos/Desktop/4TB6 - Capstone/low_ram_split/output_files/'

    pi_temp_dir ='/home/capstone/Documents/recording/temporary_files/'
    manny_temp_dir = '/Users/mannylemos/Desktop/4TB6 - Capstone/low_ram_split/temporary_files/'
    
    video_length        = 120
    num_partitions      = 10
    frames_per_second   = 30
    output_directory    = pi_output_dir
    temp_directory      = pi_temp_dir
    camera_number       = -1
    resolution          = 0
    app = video_buffer.Buffer(video_length, num_partitions, frames_per_second, output_directory, temp_directory, camera_number, resolution)
    buffer = threading.Thread(name='start_buffer', target=app.start_buffer)
    buffer.start()

    #-------------------------------------------------

    # live demo: c -> clip, s -> stop

    while (True):
        txt = input('\n(c)lip or (s)top: ')
        if txt == 'c':
            app.log_buffer()
        else:
            break
    
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

__main__()
