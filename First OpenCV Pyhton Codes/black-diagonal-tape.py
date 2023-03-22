import cv2

image=cv2.imread("Maryam-Mirzakhani.jpg")

image_2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image_2.shape)

for i in range(250):
    image_2[i, 250-i:400-i]=0

for i in range(250, 400):
    image_2[i, 0:400-i]=0

cv2.imshow("", image_2)

cv2.waitKey()

cv2.imwrite("late_maryam_mirzakhani.jpg", image_2)

