'''
Created on Mar 28, 2020

@author: Nitesh
'''

import cv2
import numpy as np

image = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\data\\coins.jpg")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#Below config for wine-glassed.jpg
#processed_img = cv2.inRange(hsv, np.array([84,14,0]), np.array([139, 113, 244]))

#Below config for coins.jpg
processed_img = cv2.inRange(hsv, np.array([0,0,176]), np.array([255, 62, 255]))

# thresh = cv2.adaptiveThreshold(processed_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 20)
# cv2.imshow('thresh', thresh)
# cv2.waitKey(0)

blurred = cv2.GaussianBlur(processed_img, (5, 5), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

edged = cv2.Canny(blurred, 50, 150)
cv2.imshow("Edges", edged)
cv2.waitKey(0)

(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("I count {} coins in this image".format(len(cnts)))
coins = image.copy()
cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
cv2.imshow('Objects', image)
cv2.waitKey(0)