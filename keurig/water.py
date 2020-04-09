import time
import RPi.GPIO as GPIO

water_pin = 22
LED1 = 17
LED2 = 27

GPIO.setmode(GPIO.BCM)
print ("water.py running")
GPIO.setup(water_pin, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

GPIO.output(water_pin, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)
time.sleep(10)
GPIO.output(water_pin, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.cleanup()
