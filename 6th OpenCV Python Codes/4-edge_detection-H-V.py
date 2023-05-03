import numpy as np
import cv2

image=cv2.imread("Input/building.png", cv2.IMREAD_GRAYSCALE)

def horizontal_edege_detection(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)

    kernel = np.array([[-1, -1, -1],
                       [0, 0, 0],
                       [1, 1, 1]])   
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            neighbor=image[i-1:i+2, j-1:j+2]
            ave=np.abs(np.sum(kernel*neighbor))
            result[i, j]=ave
    
    return result

def vertical_edege_detection(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)

    kernel = np.array([[1, 0, -1],
                       [1, 0, -1],
                       [1, 0, -1]])*2   
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            neighbor=image[i-1:i+2, j-1:j+2]
            ave=np.abs(np.sum(kernel*neighbor))
            result[i, j]=ave
    
    return result

horizontal_edege_building=horizontal_edege_detection(image)
vertical_edege_building=vertical_edege_detection(image)

cv2.imshow("H", horizontal_edege_building)
cv2.imshow("V", vertical_edege_building)
cv2.waitKey()

cv2.imwrite("Output/horizontal_edge_building.jpg", horizontal_edege_building)
cv2.imwrite("Output/vertical_edege_building.jpg", vertical_edege_building)
