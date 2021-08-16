#coding=UTF-8

#cv2.HoughCircles(image, method, dp, minDist) function to detect circles in images using OpenCV

'''
image: 8-bit, single channel image. If working with a color image, convert to grayscale first.
method: Defines the method to detect circles in images. Currently, the only implemented method is 
        cv2.HOUGH_GRADIENT, which corresponds to the Yuen et al. paper.
dp: This parameter is the inverse ratio of the accumulator resolution to the image resolution (see Yuen et al. 
    for more details). Essentially, the larger the dp gets, the smaller the accumulator array gets.
minDist: Minimum distance between the center (x, y) coordinates of detected circles. If the minDist is too small, 
        multiple circles in the same neighborhood as the original may be (falsely) detected. If the minDist is 
        too large, then some circles may not be detected at all.
param1: Gradient value used to handle edge detection in the Yuen et al. method.
param2: Accumulator threshold value for the cv2.HOUGH_GRADIENT method. The smaller the threshold is, the more 
        circles will be detected (including false circles). The larger the threshold is, the more circles will 
        potentially be returned.
minRadius: Minimum size of the radius (in pixels).
maxRadius: Maximum size of the radius (in pixels).
'''

import cv2
import numpy as np

class DetectCircle:
    def detect_circle(self, path, dp, minDist):
        image=cv2.imread(path)
        output = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
        # detect circles in the image
        circles = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, dp, minDist)
        
        # ensure at least some circles were found
        if circles is not None:
            # convert the (x, y) coordinates and radius of the circles to integers
            circles = np.round(circles[0, :]).astype("int")
            # loop over the (x, y) coordinates and radius of the circles
            for (x, y, r) in circles:
                # draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                
            # show the output image
            cv2.imshow("Original", thresh)
            cv2.imshow("output", output)
            cv2.waitKey(0)
            
o=DetectCircle()
#o.detect_circle("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\can-lid3.jpg", 1.5, 150)
#o.detect_circle("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\can-lid1.jpg", 1.2, 200)
o.detect_circle("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\can-lid2.jpg", 1.0, 160)