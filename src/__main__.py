import threading
import accelerometer.start as Accelerometer
import ultrasonic_sensor.start as Ultrasonic

accelerometer_thread = threading.Thread(name="accelerometer", target=Accelerometer.Start)
accelerometer_thread.start()

ultrasonic_thread = threading.Thread(name="ultrasonic", target=Ultrasonic.Start)
ultrasonic_thread.start()