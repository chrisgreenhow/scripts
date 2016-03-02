import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin1 = 23
led_pin2 = 24
led_pin3 = 25

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)

GPIO.output(led_pin1, False)
GPIO.output(led_pin2, False)
GPIO.output(led_pin3, False)

try:
    while True:
        GPIO.output(led_pin1, True)
        time.sleep(1)
        GPIO.output(led_pin2, True)
        time.sleep(1)
        GPIO.output(led_pin3, True)
finally:  
    GPIO.output(led_pin1, False)
    GPIO.output(led_pin2, False)
    GPIO.output(led_pin3, False)    
    GPIO.cleanup()
