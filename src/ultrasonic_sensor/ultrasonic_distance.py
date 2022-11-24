#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
LED_PIN_1 = 17
LED_PIN_2 = 22
LED_PIN_3 = 23
LED_PIN_4 = 25
LED_PIN_5 = 27

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(LED_PIN_4, GPIO.OUT)
GPIO.setup(LED_PIN_5, GPIO.OUT)

#distance calculation
min_distance = 0
max_distance = 50
partitions = 5
increment1 = (max_distance - min_distance)/partitions
increment2 = (max_distance - min_distance)/partitions*2
increment3 = (max_distance - min_distance)/partitions*3
increment4 = (max_distance - min_distance)/partitions*4
increment5 = (max_distance - min_distance)/partitions*5

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)
            if (increment1 > dist > min_distance):
                GPIO.output(LED_PIN_1, GPIO.HIGH)
                GPIO.output(LED_PIN_2, GPIO.HIGH)
                GPIO.output(LED_PIN_3, GPIO.HIGH)
                GPIO.output(LED_PIN_4, GPIO.HIGH)
                GPIO.output(LED_PIN_5, GPIO.HIGH)
                print("5")
                time.sleep(1)
            if (increment2 > dist > increment1):
                GPIO.output(LED_PIN_1, GPIO.HIGH)
                GPIO.output(LED_PIN_2, GPIO.HIGH)
                GPIO.output(LED_PIN_3, GPIO.HIGH)
                GPIO.output(LED_PIN_4, GPIO.HIGH)
                GPIO.output(LED_PIN_5, GPIO.LOW)
                print("4")
                time.sleep(1)
            if (increment3 > dist > increment2):
                GPIO.output(LED_PIN_1, GPIO.HIGH)
                GPIO.output(LED_PIN_2, GPIO.HIGH)
                GPIO.output(LED_PIN_3, GPIO.HIGH)
                GPIO.output(LED_PIN_4, GPIO.LOW)
                GPIO.output(LED_PIN_5, GPIO.LOW)
                print("3")
                time.sleep(1)
            if (increment4 > dist > increment3):
                GPIO.output(LED_PIN_1, GPIO.HIGH)
                GPIO.output(LED_PIN_2, GPIO.HIGH)
                GPIO.output(LED_PIN_3, GPIO.LOW)
                GPIO.output(LED_PIN_4, GPIO.LOW)
                GPIO.output(LED_PIN_5, GPIO.LOW)
                print("2")
                time.sleep(1)
            if (increment5 > dist > increment4):
                GPIO.output(LED_PIN_1, GPIO.HIGH)
                GPIO.output(LED_PIN_2, GPIO.LOW)
                GPIO.output(LED_PIN_3, GPIO.LOW)
                GPIO.output(LED_PIN_4, GPIO.LOW)
                GPIO.output(LED_PIN_5, GPIO.LOW)
                time.sleep(1)
                print("1")
            if (dist > increment5):
                GPIO.output(LED_PIN_1, GPIO.LOW)
                GPIO.output(LED_PIN_2, GPIO.LOW)
                GPIO.output(LED_PIN_3, GPIO.LOW)
                GPIO.output(LED_PIN_4, GPIO.LOW)
                GPIO.output(LED_PIN_5, GPIO.LOW)
                print("0")
                time.sleep(1)
            #GPIO.output(LED_PIN, GPIO.LOW)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
