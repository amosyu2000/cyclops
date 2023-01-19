import threading
import accelerometer.start as Accelerometer
import ultrasonic_sensor.start as Ultrasonic
import recording.start as Recording

isCrashed = False # parameter will be updated when a crash is detected 

accelerometer_thread = threading.Thread(name="accelerometer", target=Accelerometer.Start)
accelerometer_thread.start()

ultrasonic_thread = threading.Thread(name="ultrasonic", target=Ultrasonic.Start)
ultrasonic_thread.start()

recording_thread = threading.Thread(name="recording", target=lambda: Recording.Start(isCrashed))
recording_thread.start()