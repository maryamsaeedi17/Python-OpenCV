import numpy as np
import cv2

image=cv2.imread("Input/flower_input.jpg")
image_gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY_INV)

blur=cv2.GaussianBlur(image, (25, 25), 0)
blur[thresh==255]=[0, 0, 0]

result=cv2.bitwise_and(image, blur)

cv2.imshow("", result)
cv2.waitKey()

cv2.imwrite("Output/focus_on_foreground.jpg", result)