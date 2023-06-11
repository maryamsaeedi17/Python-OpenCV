import cv2

rubik=cv2.imread("Input/rubik.png")

rows, cols, _ = rubik.shape

for i in range(rows):
    for j in range(cols):
        b, g, r=rubik[i, j]
        if (b==0) and (g==255) and (r==255):
            b=255
            g=0
            r=0
        elif (b==255) and (g==255) and (r==0):
            b=0
            g=0
            g=255
        elif (b==255) and (g==0) and (r==255):
            b=0
            g=255
            r=0
        rubik[i, j]=b, g, r

cv2.imshow("", rubik)
cv2.waitKey()

cv2.imwrite("Output/solved_rubik.jpg", rubik)