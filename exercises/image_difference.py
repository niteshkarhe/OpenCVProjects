'''
Created on Mar 27, 2020

@author: Nitesh
'''

# import the necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils
import cv2

"""
driver = webdriver.Chrome(executable_path = 'D:\\Softwares\\eclipse-jee-oxygen-2-win32-x86_64\\ChromedriverV92\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
inp_box = driver.find_element(By.ID, "user-message")
inp_box.send_keys("Nitesh")

if(driver.find_element(By.XPATH, "//a[text()='No, thanks!']").text == "No, thanks!"):
    driver.find_element(By.XPATH, "//a[text()='No, thanks!']").click()
    
button = driver.find_element(By.XPATH, "//button[text()='Show Message']")
button.click()
#screenshot_ele = driver.find_element(By.XPATH, "//div[text()='Single Input Field']/parent::div")
screenshot_ele = driver.find_element(By.XPATH, "//body")
screenshot_ele.screenshot("D:\\NK\\API\\APIProjects\\OpenCVProjects\\exercises\\imageA.png")

inp_box.clear()
inp_box.send_keys("Pratik")
button = driver.find_element(By.XPATH, "//button[text()='Show Message']")
button.click()
screenshot_ele.screenshot("D:\\NK\\API\\APIProjects\\OpenCVProjects\\exercises\\imageB.png")
driver.quit()
"""

# load the two input images
#imageA = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\data\\modified_01.png")
#imageB = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\\data\\original_01.png")

imageA = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\exercises\\imageA.png")
(H,W, n) = imageA.shape
imageB = cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\exercises\\imageB.png")
imageB = cv2.resize(imageB, (W, H))

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

#image Difference with OpenCV and Python
# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)



# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("Original", imageA)
cv2.waitKey(0)
cv2.imshow("Modified", imageB)
cv2.waitKey(0)
cv2.imshow("Diff", diff)
cv2.waitKey(0)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)