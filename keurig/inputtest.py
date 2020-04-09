from gpiozero import Button
from time import sleep
brew_button = Button(4)
power_button = Button(3)
water_sensor = Button(2)
while True:
	if brew_button.is_pressed:
		print("Brew button pressed")
		sleep(0.25)
	if power_button.is_pressed:
		print("Power button pressed")
		sleep(.25)
	if water_sensor.is_pressed:
		print("Water is present")
		sleep(.25)
