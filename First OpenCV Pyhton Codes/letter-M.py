import numpy as np
import cv2

letter_m_array=np.empty((600,600))

for i in range(600):
    for j in range(600):
        letter_m_array[i, j]=255

#left and right lines
for i in range(100,501):
    for j,k in zip(range(80,131), range(470,521)):
        letter_m_array[i,j]=0
        letter_m_array[i,k]=0

letter_m_array[501:505, 75:135]=0
letter_m_array[501:505, 465:525]=0

#diagonal lines
for i in range(100,310):
    letter_m_array[i, i-32:i+32]=0
    letter_m_array[i, 567-i:631-i]=0

cv2.imshow("", letter_m_array)

cv2.waitKey()

cv2.imwrite("letter_M.jpg", letter_m_array)
