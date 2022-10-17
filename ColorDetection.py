import cv2
import numpy as np

cap = cv2.VideoCapture(0)
upper_limit = np. array([116,252,255])
lower_limit = np. array([99,136,136])

print("Starting")
while True:
	ret, frame = cap.read()
	hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


	c = cv2.waitKey(1)
	mask = cv2.inRange(hsv_img, lower_limit, upper_limit)


	mass_y, mass_x = np.where(mask >= 255)


	if len(mass_y)> 0:
		cent_x = np.average(mass_x)
		cent_y = np.average(mass_y)

		print(cent_x,cent_y)
		#cv2.circle(frame, [int(cent_x), int(cent_y)], 7, (0, 255, 0), -1)
	
	#cv2.imshow('frame', frame)

	#if c == 27:
		#break


cap.release()
cv2.destroyAllWindows()