import cv2
import numpy as np
import RPi.GPIO as gpio
import pigpio
import time

# sudo apt-get update && sudo apt-get install python3-pigpio
# https://ben.akrin.com/raspberry-pi-servo-jitter/

#Configuring dont show warnings 
gpio.setwarnings(False)
servopin = 4
Servo = pigpio.pi()
Servo.set_mode(servopin, pigpio.OUTPUT)
Servo.set_PWM_frequency( servopin, 50 )
ServoPostion = 800

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
		NewServoPostion = ServoPostion+yerror
		if (NewServoPostion> 800) and (NewServoPostion < 2000):
			ServoPostion = NewServoPostion
			Servo.set_servo_pulsewidth( servopin,  ServoPostion)
		print(yerror)
		#frame = cv2.putText(frame, str(int(yerror*0.1)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 2, cv2.LINE_AA)
		#cv2.circle(frame, [int(cent_x), int(cent_y)], 7, (0, 255, 0), -1)
	
	#cv2.imshow('frame', frame)

	#if c == 27:
		#break


cap.release()
cv2.destroyAllWindows()