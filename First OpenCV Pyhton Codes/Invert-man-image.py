import cv2

man_image_array=cv2.imread("2.jpg")

man_image_array2=cv2.cvtColor(man_image_array, cv2.COLOR_BGR2GRAY)

print(man_image_array2.shape)

for i in range(1202):
    for j in range(900):
        man_image_array2[i , j]=255- man_image_array2[i , j]

cv2.imshow("",man_image_array2)

cv2.waitKey()

cv2.imwrite("normal-man-pic.jpg", man_image_array2)


