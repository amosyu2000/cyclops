import video_buffer
from time import sleep
import threading

def __main__():
    pi_dir = '/home/capstone/Documents/start_camera_buffer/test_data/'
    manny_dir = '/Users/mannylemos/Desktop/4TB6 - Capstone/camera_buffer/test_data/'
    
    video_length        = 30
    frames_per_second   = 24
    save_directory      = pi_dir
    camera_number       = -1
    resolution          = 1
    
    app = video_buffer.Buffer(video_length, frames_per_second, save_directory, camera_number, resolution)
    buffer = threading.Thread(name='start_buffer', target=app.start_buffer)

    # test case 1: Does it actually work?
    buffer.start()
    sleep(video_length)
    app.log_buffer()
    app.stop_buffer()

__main__()