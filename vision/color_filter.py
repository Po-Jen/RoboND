# The code to filter for a red door. 
import cv2
import numpy as np

frame = cv2.imread("Challenge 03c T2.jpg")

#print (frame.shape)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#modify the upper and lower bounds of the filter
#to alter the filter 
lower_red = np.array([0,150,50])
upper_red = np.array([30,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask= mask)
#print (res.shape)

cv2.imshow('frame',frame)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
