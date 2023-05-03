import numpy as np
import cv2

image_lion=cv2.imread("Input\lion.png", cv2.IMREAD_GRAYSCALE)
image_spider=cv2.imread("Input\spider.jpg", cv2.IMREAD_GRAYSCALE)


def edege_detection(image):
    rows, cols=image.shape
    result=np.zeros((rows, cols), dtype=np.uint8)

    # kernel = np.array([[-1, -1, -1],
    #                    [-1, 8, -1],
    #                    [-1, -1, -1]])

    kernel = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])   
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            neighbor=image[i-1:i+2, j-1:j+2]
            ave=np.abs(np.sum(kernel*neighbor))
            #ave=np.sum(kernel*neighbor)
            result[i, j]=ave
    
    return result

#image_lion_edge=edege_detection(image_lion)
image_spider_edge=edege_detection(image_spider)

cv2.imshow("", image_spider_edge)
#cv2.imshow("", image_lion_edge)
cv2.waitKey()

#cv2.imwrite("Output\lion_edge.jpg", image_lion_edge)
cv2.imwrite("Output\spider_edge.jpg", image_spider_edge)