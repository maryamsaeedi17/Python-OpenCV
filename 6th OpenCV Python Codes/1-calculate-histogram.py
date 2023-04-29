import numpy as np
import matplotlib.pyplot as plt
import cv2

image=cv2.imread("Input/anoushe_ansari.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols=image.shape
color_number=[]
histogram=[]
c=0
for k in range(256):
    for i in range(rows):
        for j in range(cols):
            if image[i][j]==k:
                c+=1
    histogram.append(c)
    c=0
    color_number.append(k)

#plt.plot(histogram)
plt.hist(image.ravel(), 256)
#plt.bar(color_number ,histogram)
plt.show()
            