import os 
from gpiozero import Button
from gpiozero import LED #outputs will all be set as LEDs
import time

brew_button = Button(4)
power_button = Button(3)
water_sensor = Button(2)
water_pump = LED(22)
LED2 = LED(27)
LED1 = LED(17)

#power_button = Button(3)

while True:
    if brew_button.is_pressed:
        print("Watering")
        os.system("mosquitto_pub -h 192.168.0.13 -t \"test\" -m \"watering button pushed\"")
        water_pump.on()
        LED2.on()
        time.sleep(10)
        water_pump.off()
        LED2.off()
    if water_sensor.is_pressed: #ideally the sensor would turn on/of intermittently
        print("OK water level")
        os.system("mosquitto_pub -h 192.168.0.13 -t \"test\" -m \"Water level OK\"")
        LED1.off()
        time.sleep(.5)
    if power_button.is_pressed:
        print("power button pressed")
        os.system("mosquitto_pub -h 192.168.0.13 -t \"test\" -m \"button check - water routine running\"")
        time.sleep(.5)
    else:
        print("Low Water level")
        os.system("mosquitto_pub -h 192.168.0.13 -t \"test\" -m \"I'm thirstyyyyyy!!!\"")
        LED1.on()
        time.sleep(.5)
