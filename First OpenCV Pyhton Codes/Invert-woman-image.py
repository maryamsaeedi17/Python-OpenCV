import cv2

woman_image_array=cv2.imread("1.jpg")

woman_image_array2=cv2.cvtColor(woman_image_array, cv2.COLOR_BGR2GRAY)

print(woman_image_array2.shape)

for i in range(645):
    for j in range(645):
        woman_image_array2[i , j]=255- woman_image_array2[i , j]

cv2.imshow("",woman_image_array2)

cv2.waitKey()

cv2.imwrite("normal-woman-pic.jpg", woman_image_array2)


