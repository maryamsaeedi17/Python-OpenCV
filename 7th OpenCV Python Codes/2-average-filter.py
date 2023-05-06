import numpy as np
import cv2

image1=cv2.imread("Input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
image2=cv2.imread("Input/board_noisy.png", cv2.IMREAD_GRAYSCALE)
image3=cv2.imread("Input/image_noisy.png", cv2.IMREAD_GRAYSCALE)
image4=cv2.imread("Input/spaces_balloons_noisy.jpg")
image5=cv2.imread("Input/spaces_Medianfilter.jpg", cv2.IMREAD_GRAYSCALE)
image6=cv2.imread("Input/spaces.jpg", cv2.IMREAD_GRAYSCALE)

result1=cv2.medianBlur(image1, 3)
result1_1=cv2.medianBlur(result1, 3)
result2=cv2.medianBlur(image2, 3)
result2_1=cv2.medianBlur(result2, 3)
result3=cv2.medianBlur(image3, 3)
result3_1=cv2.medianBlur(result3, 3)
result4=cv2.medianBlur(image4, 3)
result4_2=cv2.medianBlur(cv2.medianBlur(result4, 3), 3)
result5_2=cv2.medianBlur(cv2.medianBlur(image5, 3), 3)
result5_4=cv2.medianBlur(cv2.medianBlur(result5_2, 3), 3)
result6=cv2.medianBlur(image6, 3)

# cv2.imshow("r5", result5_4)
# cv2.imshow("r6", result6)
# cv2.waitKey()

cv2.imwrite("Output/xray.jpg", result1_1)
cv2.imwrite("Output/board.jpg", result2_1)
cv2.imwrite("Output/image.jpg", result3_1)
cv2.imwrite("Output/baloon.jpg", result4_2)
cv2.imwrite("Output/lady.jpg", result5_4)
cv2.imwrite("Output/character.jpg", result6)
