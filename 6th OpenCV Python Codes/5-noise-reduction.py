import numpy as np
import cv2

image1=cv2.imread("Input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
image2=cv2.imread("Input/board_noisy.png", cv2.IMREAD_GRAYSCALE)
image3=cv2.imread("Input/image_noisy.png", cv2.IMREAD_GRAYSCALE)

def noise_reduction_3in3(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            neighbor=image[i-1:i+2, j-1:j+2]
            ave=np.mean(neighbor)
            result[i, j]=ave
    return result

def noise_reduction_5in5(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)
    for i in range(2, rows-2):
        for j in range(2, cols-2):
            neighbor=image[i-2:i+3, j-2:j+3]
            ave=np.mean(neighbor)
            result[i, j]=ave
    return result


def noise_reduction_15in15(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)
    for i in range(7, rows-7):
        for j in range(7, cols-7):
            neighbor=image[i-7:i+8, j-7:j+8]
            ave=np.mean(neighbor)
            result[i, j]=ave
    return result

result1_1=noise_reduction_3in3(image1)
result1_2=noise_reduction_5in5(image1)
result1_3=noise_reduction_15in15(image1)

result2_1=noise_reduction_3in3(image2)
result2_2=noise_reduction_5in5(image2)
result2_3=noise_reduction_15in15(image2)

result3_1=noise_reduction_3in3(image3)
result3_2=noise_reduction_5in5(image3)
result3_3=noise_reduction_15in15(image3)

# cv2.imshow("result1", result3_1)
# cv2.imshow("result2", result3_2)
# cv2.imshow("result3", result3_3)
# cv2.waitKey()

cv2.imwrite("Output/xray_3in3.jpg", result1_1)
cv2.imwrite("Output/xray_5in5.jpg", result1_2)
cv2.imwrite("Output/xray_15in15.jpg", result1_3)

cv2.imwrite("Output/board_3in3.jpg", result2_1)
cv2.imwrite("Output/board_5in5.jpg", result2_2)
cv2.imwrite("Output/board_15in15.jpg", result2_3)

cv2.imwrite("Output/image_3in3.jpg", result3_1)
cv2.imwrite("Output/image_5in5.jpg", result3_2)
cv2.imwrite("Output/image_15in15.jpg", result3_3)