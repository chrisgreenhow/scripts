import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin1 = 23
led_pin2 = 24
led_pin3 = 25

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)

try:
    print("LEDs ON")
    while True:
        GPIO.output(led_pin1, True)
        time.sleep(1)
        GPIO.output(led_pin2, True)
        time.sleep(1)
        GPIO.output(led_pin3, True)
finally:  
    print("LEDs OFF")
    GPIO.cleanup()
