'''
Created on Apr 1, 2020

@author: Nitesh
'''

import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+str(y) 
        cv2.putText(img, strXY, (x, y), font, 0.5, (0, 0, 255), 2)
        cv2.imshow('image', img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        BGR = str(blue) + ', '+str(green)+' ,'+str(red)
        cv2.putText(img, BGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)
        
    if flags == (cv2.EVENT_FLAG_SHIFTKEY + cv2.EVENT_FLAG_LBUTTON):
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        cv2.imshow('image', img)
        
img = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\hog_object_detection\\car_1.jpg")
cv2.imshow('image', img)
points=[]
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()