import cv2
import numpy as np

def bgr2grayscale(image):
    b, g, r=cv2.split(image)
    result=np.zeros(image.shape[:2], dtype=np.uint8)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            result[i, j]=b[i, j]//3 + g[i, j]//3 + r[i, j]//3
    
    return result
        


bgr_image=cv2.imread("Input/butterfly.jpg")
gray_image=bgr2grayscale(bgr_image)

cv2.imshow("", gray_image)
cv2.waitKey()

cv2.imwrite("Output/gray_butterfly.jpg", gray_image)