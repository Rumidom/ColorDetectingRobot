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

#Configuring GPIO
#gpio.setmode(gpio.BCM)

#Servo
#gpio.setup(4,gpio.OUT)
#Servo = gpio.PWM(4,50)
#Servo.start(2)

for i in range(800,2000,10):
	Servo.set_servo_pulsewidth( servopin, i )
	time.sleep(0.1)


for i in range(2000,800,-10):
	Servo.set_servo_pulsewidth( servopin, i )
	time.sleep(0.1)