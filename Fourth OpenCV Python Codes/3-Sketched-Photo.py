import cv2

image = cv2.imread("Maryam_Mirzakhani.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

inv_image = 255 - image
blurred=cv2.GaussianBlur(inv_image, (21, 21), 0)
inv_blurred = 255 - blurred

for i in range(inv_blurred.shape[0]):
    for j in range(inv_blurred.shape[1]):
        if inv_blurred[i][j]==0:
            inv_blurred[i][j]=1

sketch = image / inv_blurred

sketch = sketch * 255

cv2.imshow("", sketch)
cv2.waitKey()

cv2.imwrite("sketched_photo.jpg", sketch)



