import cv2

watermelon_image=cv2.imread("Input\watermelon.jpg")

b, g, r=cv2.split(watermelon_image)

materwelon_image=cv2.merge((b, r, g))

cv2.imshow("", materwelon_image)
cv2.waitKey()

cv2.imwrite("Output\materwelon.jpg", materwelon_image)