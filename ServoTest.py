import RPi.GPIO as gpio
import time


#Configuring dont show warnings 
gpio.setwarnings(False)


#Configuring GPIO
gpio.setmode(gpio.BCM)

#Servo
gpio.setup(4,gpio.OUT)
Servo = gpio.PWM(4,50)
Servo.start(0)

for i in range(17):
	Servo.ChangeDutyCycle(i)
	time.sleep(0.5)