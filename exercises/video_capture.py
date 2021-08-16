'''
Created on Apr 1, 2020

@author: Nitesh
'''
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\opencv-object-tracking\\nascar_01.mp4")
#File name path can be given as argument
#otherwise "0" or "-1" is given to capture video from device camera. 0 for 1st camera, 1 for 2nd camera etc.

print(cap.isOpened())
#To check if video is opened

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\opencv-object-tracking\\demo_vid.mp4", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    #read(): It returns frame if is available and will be saved in frame
    #ret: True or False depends on frame is available or not
    if ret==True:
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        gray_img=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(gray_img)
        cv2.imshow('frame', gray_img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
    '''
    To get video properties
    https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    '''
    
cap.release()
out.release()
#To release all resources
cv2.destroyAllWindows()