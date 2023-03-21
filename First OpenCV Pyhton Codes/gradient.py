import numpy as np
import cv2

gradient_array=np.empty((765,765))

color=255

for i in range(0,765,3):
    gradient_array[i:i+3 , 0:765]=color
    color -= 1

cv2.imshow("", gradient_array)

cv2.waitKey()

cv2.imwrite("gradient.jpg", gradient_array)
