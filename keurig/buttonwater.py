from gpiozero import Button
from gpiozero import LED #outputs will all be set as LEDs
import time

brew_button = Button(4)
water_sensor = Button(2)
water_pump = LED(22)
LED2 = LED(27)
LED1 = LED(17)

#power_button = Button(3)

while True:
    if brew_button.is_pressed:
        print("Watering")
        water_pump.on()
        LED2.on()
        time.sleep(10)
        water_pump.off()
        LED2.off()
    if water_sensor.is_pressed: #ideally the sensor would turn on/of intermittently
        print("OK water level")
        LED1.off()
        time.sleep(.2)
    else:
        print("Low Water level")
        LED1.on()
        time.sleep(.2)
