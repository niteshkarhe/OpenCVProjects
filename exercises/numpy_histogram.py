#coding=utf-8
#The Numpy histogram function has two parameters called bins and input arrays. 
#The bins are rectangular shaped blocks which are distanced at equal horizontal 
#width that correspond to the respective class interval. 
#The difference in the height of these beans is representative of the difference 
#in the frequency of these class intervals.

'''
The Numpy histogram function doesn't draw the histogram, but it computes the occurrences of input data that 
fall within each bin, which in turns determines the area (not necessarily the height if the bins aren't of 
equal width) of each bar.
'''

import numpy as np
import matplotlib.pyplot as plt

(hist, bin_edges)=np.histogram([1, 2, 1], bins=[0, 1, 2, 3])

#There are 3 bins, for values ranging from 0 to 1 (excl 1.), 1 to 2 (excl. 2) and 2 to 3 (incl. 3), respectively.
#The input values are 1, 2 and 1. 
#0 to 1 (excl. 1): 0 occurrences of any element from input
#1 to 2 (excl. 2): 2 occurrences of 1 from input
#2 to 3 (incl. 3): 1 occurrence of 2 from input

#resulting histogram distribution -> array([0 2 1])
print('Histogram:', hist)
# plt.hist([1, 2, 1], bins=[0, 1, 2, 3])
# plt.show()

plt.bar(bin_edges[:-1], hist, width = 1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()   