import numpy as np
import cv2

#chess_board_array=[[0 for i in range(800)] for j in range(800)]

chess_board_array=np.empty((800,800))

#print(chess_board_array)

row=1

for i in range(1, 801, 100):
    if row%2 !=0:
        for j in range(1, 801, 200):
            chess_board_array[i:i+99 , j:j+99]=255
        row+=1
    else:
        for j in range(101, 801, 200):
            chess_board_array[i:i+99 , j:j+99]=255
        row+=1

cv2.imshow("sss", chess_board_array)

cv2.waitKey()

cv2.imwrite("chess_board.jpg", chess_board_array)
