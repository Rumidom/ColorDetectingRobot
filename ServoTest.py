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

for i in range(3,10,1):
	Servo.ChangeDutyCycle(i)
	time.sleep(0.25)
	Servo.ChangeDutyCycle(50)
	time.sleep(2)

for i in range(10,3,-1):
	Servo.ChangeDutyCycle(i)
	time.sleep(0.25)
	Servo.ChangeDutyCycle(50)
	time.sleep(2)