import numpy as np
import cv2

background=np.ones((600, 800, 3))*255

cv2.circle(background, (400, 500), 250, (0, 0, 255), -1)
cv2.circle(background, (400, 500), 230, (0, 160, 255), -1)
cv2.circle(background, (400, 500), 210, (0, 255, 255), -1)
cv2.circle(background, (400, 500), 190, (0, 130, 0), -1)
cv2.circle(background, (400, 500), 170, (255, 250, 0), -1)
cv2.circle(background, (400, 500), 150, (255, 0, 0), -1)
cv2.circle(background, (400, 500), 130, (133, 0, 140), -1)
cv2.circle(background, (400, 500), 110, (255, 255, 255), -1)


cv2.rectangle(background, (0, 500), (800, 600), (255, 255, 255), -1)

cv2.imshow("", background)
cv2.waitKey()

cv2.imwrite("Output/rainbow.jpg", background)
