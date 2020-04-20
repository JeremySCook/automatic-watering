#by Jeremy S. Cook 4/20/2020
#comment out lines with "mosquitto_pub" and import os if not using MQTT

import os
import time
import RPi.GPIO as GPIO

water_pin = 22
LED1 = 17
LED2 = 27

GPIO.setmode(GPIO.BCM)
print ("water.py running")
os.system("mosquitto_pub -h [BROKER_IPADDRESS] -t \"test\" -m \"watering\"") 
GPIO.setup(water_pin, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

GPIO.output(water_pin, GPIO.HIGH)
GPIO.output(LED2, GPIO.HIGH)
time.sleep(10)
os.system("mosquitto_pub -h [BROKER_IPADDRESS] -t \"test\" -m \"done watering\"")
GPIO.output(water_pin, GPIO.LOW)
GPIO.output(LED2, GPIO.LOW)
GPIO.cleanup()
