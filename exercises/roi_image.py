'''
Created on Apr 1, 2020

@author: Nitesh
'''
import cv2
import numpy as np

img = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\data\\messi.jpg")
img_copy_1=np.copy(img)
img_copy_2=np.copy(img)
face_coord = img[448:38, 707:293]

draw_rect = cv2.rectangle(img_copy_1, (448, 38), (707,293), (0,0,255), 3)

cv2.imshow('face_detection', draw_rect)
cv2.waitKey(0)

dst=cv2.addWeighted(img_copy_2, 0.9, img_copy_1, 0.1, 0)
cv2.imshow('add_wighted', dst)
cv2.waitKey(0)