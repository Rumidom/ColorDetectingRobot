import RPi.GPIO as gpio
import time


#Configuring dont show warnings 
gpio.setwarnings(False)


#Configuring GPIO
pio.setmode(gpio.BCM)

#Left Motor
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)
LeftFoward = gpio.PWM(20,100)
LeftBackwards = gpio.PWM(21,100)
LeftBackwards.start(0)
LeftFoward.start(0)

def LeftMotorMove(value):
	if value > 0:
		LeftBackwards.ChangeDutyCycle(0) 
		LeftFoward.ChangeDutyCycle(value)
	else if value < 0:
		LeftFoward.ChangeDutyCycle(0) 
		LeftBackwards.ChangeDutyCycle(abs(value))
	else if value == 0:
		LeftBackwards.ChangeDutyCycle(0) 
		LeftFoward.ChangeDutyCycle(0) 

#Right Motor
gpio.setup(19,gpio.OUT)
gpio.setup(16,gpio.OUT)
RightFoward = gpio.PWM(16,100)
RightBackwards = gpio.PWM(19,100)
RightBackwards.start(0)
RightFoward.start(0)

def RightMotorMove(value):
	if value > 0:
		RightBackwards.ChangeDutyCycle(0) 
		RightFoward.ChangeDutyCycle(value)
	elif value < 0:
		RightFoward.ChangeDutyCycle(0) 
		RightBackwards.ChangeDutyCycle(abs(value))
	elif value == 0:
		RightBackwards.ChangeDutyCycle(0) 
		RightFoward.ChangeDutyCycle(0) 

LeftMotorMove(100)
time.sleep(2)
LeftMotorMove(-100)
time.sleep(2)
LeftMotorMove(0)
time.sleep(2)
RightMotorMove(100)
time.sleep(2)
RightMotorMove(-100)
time.sleep(2)
RightMotorMove(0)