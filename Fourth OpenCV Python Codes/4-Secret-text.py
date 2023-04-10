import cv2
import numpy as np

text1=cv2.imread("st1.jpg")
text2=cv2.imread("st2.jpg")

text1=255- text1
text2=255- text2

secret_text= text1 - text2

secret_text=255- secret_text

cv2.imshow("", secret_text)
cv2.waitKey()

cv2.imwrite("secret_text.jpg", secret_text)