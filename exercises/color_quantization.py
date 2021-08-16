#coding=UTF-8
#Color quantization is the process of reducing the number of distinct colors in an image.

'''Normally, the intent is to preserve the color appearance of the image as much as possible, while reducing 
the number of colors, whether for memory limitations or compression.'''

from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import KMeans
import numpy as np
import cv2

#MiniBatchKMeans is substantially faster than normal K-Means, although the centroids may not be as stable

'''
This is because MiniBatchKMeans operates on small “batches” of the dataset, whereas K-Means operates on the 
population of the dataset, thus making the mean calculation of each centroid, as well as the centroid update loop,
much slower.
'''

image=cv2.imread("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\breaking-bad.jpg")
(h, w) = image.shape[:2]

# convert the image from the RGB color space to the L*a*b*
# color space -- since we will be clustering using k-means
# which is based on the euclidean distance, we'll use the
# L*a*b* color space where the euclidean distance implies
# perceptual meaning
image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# reshape the image into a feature vector so that k-means can be applied
image = image.reshape((image.shape[0] * image.shape[1], 3))

# apply k-means using the specified number of clusters and
# then create the quantized image based on the predictions
clt = MiniBatchKMeans(n_clusters = 8)
labels = clt.fit_predict(image)
quant = clt.cluster_centers_.astype("uint8")[labels]
# clt = KMeans(n_clusters = 3)
# labels = clt.fit_predict(image)
# quant = clt.cluster_centers_.astype("uint8")[labels]

# reshape the feature vectors to images
quant = quant.reshape((h, w, 3))
image = image.reshape((h, w, 3))

# convert from L*a*b* to RGB
quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)

# display the images and wait for a keypress
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.namedWindow('quant', cv2.WINDOW_NORMAL)
cv2.imshow("quant", quant)
cv2.waitKey(0)