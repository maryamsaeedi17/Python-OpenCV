import cv2

image=cv2.imread("3.jpg")

image_2=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(image_2.shape)

for i in range(705):
    for j in range(1280//2):
        image_2[i,j]=image_2[i,1279-j]

for i in range(705//2):
    temp=image_2[i, 0:1280]
    image_2[i, 0:1280]=image_2[704-i , 0:1280]
    image_2[704-i , 0:1280]=temp


cv2.imshow("", image_2)

cv2.waitKey()

cv2.imwrite("rotate_180_degree.jpg", image_2)
