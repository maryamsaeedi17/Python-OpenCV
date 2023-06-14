import numpy as np
import cv2


watermelon_image=cv2.imread("Input/watermelon.jpg")
watermelon_image=cv2.cvtColor(watermelon_image, cv2.COLOR_BGR2HSV)

h, s, v=cv2.split(watermelon_image)

h_new = h.copy().astype(np.float32)


for i in range(h.shape[0]):
    for j in range(h.shape[1]):
        if 30 < h[i,j] < 80:
            h_new[i,j] -= 35
        if h_new[i,j] < 0:
            h_new[i, j] +=180
        if h[i,j] < 15 or h[i,j] > 165:
            h_new[i,j] += 70
        if h_new[i,j] > 180:
            h_new[i,j] -=180
        


h_new=h_new.astype(np.uint8)

materwelon_image=cv2.merge((h_new, s, v))
materwelon_image=cv2.cvtColor(materwelon_image, cv2.COLOR_HSV2BGR)

cv2.imshow("", materwelon_image)
cv2.waitKey()

cv2.imwrite("Output/materwelon-HSV.jpg", materwelon_image)