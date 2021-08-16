import cv2
import numpy as np

image=cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\data\\coins.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#Below config for wine-glassed.jpg
#processed_img = cv2.inRange(hsv, np.array([84,14,0]), np.array([139, 113, 244]))

##Below config for coins.jpg
processed_img = cv2.inRange(hsv, np.array([0,0,176]), np.array([255, 62, 255]))

cv2.imshow('hsv_processed', processed_img)
cv2.waitKey(0)

thresh = cv2.adaptiveThreshold(processed_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 20)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)