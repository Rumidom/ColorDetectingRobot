import cv2
import numpy as np
import RPi.GPIO as gpio
import pigpio
import time

# sudo apt-get update && sudo apt-get install python3-pigpio
# https://ben.akrin.com/raspberry-pi-servo-jitter/
gpio.setmode(gpio.BCM)
#Configuring dont show warnings 
gpio.setwarnings(False)

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
	elif value < 0:
		LeftFoward.ChangeDutyCycle(0) 
		LeftBackwards.ChangeDutyCycle(abs(value))
	elif value == 0:
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


servopin = 4
Servo = pigpio.pi()
Servo.set_mode(servopin, pigpio.OUTPUT)
Servo.set_PWM_frequency( servopin, 50 )
ServoPostion = 1200
RobotRotation = 0
Servo.set_servo_pulsewidth( servopin,  ServoPostion)
cap = cv2.VideoCapture(0)
Upper_Limit = np. array([117,255,201])
Lower_Limit = np. array([101,71,47])
ret, frame = cap.read()
print(frame.shape)
width = frame.shape[1]
height = frame.shape[0]
print("Starting")

while True:

	ret, frame = cap.read()
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	#c = cv2.waitKey(1)
	mask = cv2.inRange(hsv_img, Lower_Limit, Upper_Limit)


	mass_y, mass_x = np.where(mask >= 255)


	if len(mass_y)> 0:
		cent_x = np.average(mass_x)
		cent_y = np.average(mass_y)
		yerror = cent_y - (height/2)
		xerror = cent_x - (width/2)
		AreaError = 23000 - len(mass_y)

		NewServoPostion = ServoPostion+int(yerror*0.1)
		if (NewServoPostion> 800) and (NewServoPostion < 2000):
			ServoPostion = NewServoPostion
			Servo.set_servo_pulsewidth( servopin,  ServoPostion)
		
		RobotRotation = int(xerror*0.7)
		if RobotRotation > 100:
			RobotRotation = 100
		if RobotRotation < -100:
			RobotRotation = -100

		if abs(RobotRotation) > 10 and abs(yerror) < 20:
			LeftMotorMove(-RobotRotation)
			RightMotorMove(RobotRotation)
			time.sleep(0.02)
			LeftMotorMove(0)
			RightMotorMove(0)

		RobotMovement = (AreaError * (1/100))

		if RobotMovement > 100:
			RobotMovement = 100
		if RobotMovement < -100:
			RobotMovement = -100

		if abs(RobotMovement) > 10 and abs(yerror) < 20:
			LeftMotorMove(RobotMovement)
			RightMotorMove(RobotMovement)
			time.sleep(0.02)
			LeftMotorMove(0)
			RightMotorMove(0)

		print(yerror,xerror,AreaError)
		#frame = cv2.putText(frame, str(int(yerror*0.1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)
		#cv2.circle(frame, [int(cent_x), int(cent_y)], 7, (0, 255, 0), -1)
	
	#cv2.imshow('frame', frame)

	#if c == 27:
		#break


cap.release()
cv2.destroyAllWindows()