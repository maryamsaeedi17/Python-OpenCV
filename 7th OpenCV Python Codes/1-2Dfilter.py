import numpy as np
import cv2

image=cv2.imread("Input/flower.jpg", cv2.IMREAD_GRAYSCALE)

# 1. Edge detection filter
kernel_ed = np.array([[-1 , -1 , -1],
                      [-1 ,  8 , -1],
                      [-1 , -1 , -1]])

# 2. Sharpening filter
kernel_sh = np.array([[0  , -1 ,  0],
                      [-1 ,  5 , -1],
                      [0  , -1 ,  0]])

# 3. Emboss filter
kernel_em = np.array([[-2 , -1 ,  0],
                      [-1 ,  1 ,  1],
                      [0  ,  1 ,  2]])

# 4. Identity filter
kernel_id = np.array([[0  ,  0 ,  0],
                      [0  ,  1 ,  0],
                      [0  ,  0 ,  0]])

# 5. Your filter
my_kernel = np.array([[-1  , 0 ,  -1],
                      [0  ,  5  ,  0],
                      [-1  , 0 ,  -1]])

image_1= cv2.filter2D(image, -1,   kernel_ed)      
image_2= cv2.filter2D(image, -1,   kernel_sh)      
image_3= cv2.filter2D(image, -1,   kernel_em)      
image_4= cv2.filter2D(image, -1,   kernel_id)      
image_5= cv2.filter2D(image, -1, my_kernel)

# cv2.imshow("1", image_1)
# cv2.imshow("2", image_2)
# cv2.imshow("3", image_3)
# cv2.imshow("4", image_4)
# cv2.imshow("5", image_5)
# cv2.waitKey()

result_1=np.hstack((image, image_1))
result_2=np.hstack((image, image_2))
result_3=np.hstack((image, image_3))
result_4=np.hstack((image, image_4))
result_5=np.hstack((image, image_5))

# cv2.imshow("result", result_2)
# cv2.waitKey()

cv2.imwrite("Output/2Dfilter_edge_detection.jpg", result_1)
cv2.imwrite("Output/2Dfilter_sharpening.jpg", result_2)
cv2.imwrite("Output/2Dfilter_emboss.jpg", result_3)
cv2.imwrite("Output/2Dfilter_identity.jpg", result_4)
cv2.imwrite("Output/my2Dfilter.jpg", result_5)