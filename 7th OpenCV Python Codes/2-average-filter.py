import numpy as np
import cv2

image=cv2.imread("Input/squares.jpg", cv2.IMREAD_GRAYSCALE)

ker1 = np.array([[ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04, 0.04, 0.04]])

ker2 = np.array([[ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1],
                 [ 1, 1, 1, 1, 1]])

ker3 = np.array([[ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5],
                 [ 5, 5, 5, 5, 5]])

ker4 = np.array([[ 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04],
                 [ 0.04, 0.04, 0.04]])

ker5 = np.array([[ 1, 1, 1],
                 [ 1, 1, 1],
                 [ 1, 1, 1]])

ker6 = np.array([[ 5, 5, 5],
                 [ 5, 5, 5],
                 [ 5, 5, 5]])


result1   = cv2.filter2D(image, -1,   ker1)      
result2   = cv2.filter2D(image, -1,   ker2)      
result3   = cv2.filter2D(image, -1,   ker3)      
result4   = cv2.filter2D(image, -1,   ker4) 
result5   = cv2.filter2D(image, -1,   ker5)      
result6   = cv2.filter2D(image, -1,   ker6) 

result = np.hstack((image, result1, result2, result3, result4, result5, result6))

# cv2.imshow("r1", result1)
# cv2.imshow("r2", result2)
# cv2.imshow("r3", result3)
# cv2.imshow("r4", result4)
# cv2.imshow("r", result)
# cv2.waitKey()

cv2.imwrite("Output/hidden_character.jpg", result)