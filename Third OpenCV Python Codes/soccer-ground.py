import cv2
import numpy as np

ground=np.zeros((500, 700, 3), np.uint8)

for i in range(7):
    if i%2==0:
        cv2.rectangle(ground, (100*i, 0), (100*(i+1), 500), (0,128,0), -1)
    elif i%2!=0:
        cv2.rectangle(ground, (100*i, 0), (100*(i+1), 500), (0,255,0), -1)

cv2.line(ground, (350, 20), (350, 480), (255, 255, 255), 2)

cv2.rectangle(ground, (20, 20), (680, 480), (255, 255, 255), 2)

cv2.rectangle(ground, (20, 190), (80, 325), (255, 255, 255), 2)
cv2.rectangle(ground, (620, 190), (680, 325), (255, 255, 255), 2)

cv2.rectangle(ground, (20, 135), (140, 380), (255, 255, 255), 2)
cv2.rectangle(ground, (560, 135), (680, 380), (255, 255, 255), 2)

cv2.circle(ground, (350, 250), 80, (255, 255, 255), 2)
cv2.circle(ground, (350, 250), 5, (255, 255, 255), -1)

cv2.imshow("soccer ground", ground)
cv2.waitKey()

cv2.imwrite("soccer_groud.jpg", ground)