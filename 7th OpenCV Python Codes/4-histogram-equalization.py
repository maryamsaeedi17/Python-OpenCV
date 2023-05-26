import cv2
import matplotlib.pyplot as plt

image1=cv2.imread("Input/Unequalized_Hawkes_Bay_NZ.jpg", cv2.IMREAD_GRAYSCALE)
# image2=cv2.imread("Input/from_sky.jpg", cv2.IMREAD_GRAYSCALE)
# image3=cv2.imread("Input/lab.jpg", cv2.IMREAD_GRAYSCALE)

image1_ok=cv2.equalizeHist(image1)

# hist1=cv2.calcHist([image1], [0], None, [256], [0, 256])
hist1_1=cv2.calcHist([image1_ok], [0], None, [256], [0, 256])
# plt.plot(hist1)
plt.plot(hist1_1)
plt.show()