#coding=UTF-8
#https://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2
import numpy as np

class ColorClustering():
    def color_clustering(self, path):
        image=cv2.imread(path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # show our image
        plt.figure()
        plt.axis("off")
        plt.imshow(image)
        plt.waitforbuttonpress()
         
        #our goal is to generate k clusters from n data points. We will be treating our MxN image as our 
        #data points.
        #In order to do this, we need to re-shape our image to be a list of pixels, rather than MxN matrix of 
        #pixels
        
        # reshape the image to be a list of pixels values, a 1 D array
        image = image.reshape((image.shape[0] * image.shape[1], 3))
        
        # cluster the pixel intensities and find the most dominant colors in an image
        clt = KMeans(n_clusters = 3) #This will create 3 clusters
        clt.fit(image) #Our image pixel will fit into 3 clusters with each cluster will be having only one type 
                       #of color
        print('np.unique(clt.labels_):',np.unique(clt.labels_)) #Each data item (pixel) will be given with one of the cluster label
        # build a histogram of clusters and then create a figure
        # representing the number of pixels labeled to each color
        hist = self.centroid_histogram(clt)
        bar = self.plot_colors(hist, clt.cluster_centers_)
        # show our color bart
        plt.figure()
        plt.axis("off")
        plt.imshow(bar)
        plt.show()

    def centroid_histogram(self, clt):
        # grab the number of different clusters and create a histogram
        # based on the number of pixels assigned to each cluster
        numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
        (hist, _) = np.histogram(clt.labels_, bins = numLabels)
        # normalize the histogram, such that it sums to one
        hist = hist.astype("float")
        hist /= hist.sum()
        plt.hist(clt.labels_, numLabels)
        plt.show()
        # return the histogram
        return hist
    
    def plot_colors(self, hist, centroids):
        # initialize the bar chart representing the relative frequency
        # of each of the colors
        bar = np.zeros((50, 300, 3), dtype = "uint8")
        startX = 0
        # loop over the percentage of each cluster and the color of
        # each cluster
        for (percent, color) in zip(hist, centroids):
            # plot the relative percentage of each cluster
            endX = startX + (percent * 300)
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),color.astype("uint8").tolist(), -1)
            startX = endX
        
        # return the bar chart
        return bar
    
o=ColorClustering()
o.color_clustering("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\jurassic_poster.png")
o.color_clustering("D:\\NK\\API\\APIProjects\\OpenCVProjects\\tests\data\\batman.jpg")