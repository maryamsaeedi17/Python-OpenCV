import cv2

bat_image=cv2.imread("bat.jpg")
bat_image=cv2.cvtColor(bat_image, cv2.COLOR_BGR2GRAY)

print(bat_image.shape)

threshold=127

_, bat_image=cv2.threshold(bat_image, threshold, 255, cv2.THRESH_BINARY_INV)

cv2.putText(bat_image, "BATMAN", (360, 500), cv2.FONT_HERSHEY_COMPLEX, 2, 255, thickness = 3)

cv2.imshow("", bat_image)
cv2.waitKey()


cv2.imwrite("batman_logo.jpg", bat_image)