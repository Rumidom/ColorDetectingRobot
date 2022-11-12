import RPi.GPIO as gpio
import time


#Configuring dont show warnings 
gpio.setwarnings(False)


#Configuring GPIO
gpio.setmode(gpio.BCM)

#Servo
gpio.setup(4,gpio.OUT)
Servo = gpio.PWM(4,50)
Servo.start(2)

for i in range(2,12,-1):
	Servo.ChangeDutyCycle(i)
	time.sleep(0.5)

for i in range(12,2,-1):
	Servo.ChangeDutyCycle(i)
	time.sleep(0.5)