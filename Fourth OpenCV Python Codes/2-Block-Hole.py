import numpy as np
import cv2

q_1_1=cv2.imread("black_hole/1/1.jpg").astype(np.float32)
q_1_2=cv2.imread("black_hole/1/2.jpg").astype(np.float32)
q_1_3=cv2.imread("black_hole/1/3.jpg").astype(np.float32)
q_1_4=cv2.imread("black_hole/1/4.jpg").astype(np.float32)
q_1_5=cv2.imread("black_hole/1/5.jpg").astype(np.float32)

q_2_1=cv2.imread("black_hole/2/1.jpg").astype(np.float32)
q_2_2=cv2.imread("black_hole/2/2.jpg").astype(np.float32)
q_2_3=cv2.imread("black_hole/2/3.jpg").astype(np.float32)
q_2_4=cv2.imread("black_hole/2/4.jpg").astype(np.float32)
q_2_5=cv2.imread("black_hole/2/5.jpg").astype(np.float32)

q_3_1=cv2.imread("black_hole/3/1.jpg").astype(np.float32)
q_3_2=cv2.imread("black_hole/3/2.jpg").astype(np.float32)
q_3_3=cv2.imread("black_hole/3/3.jpg").astype(np.float32)
q_3_4=cv2.imread("black_hole/3/4.jpg").astype(np.float32)
q_3_5=cv2.imread("black_hole/3/5.jpg").astype(np.float32)

q_4_1=cv2.imread("black_hole/4/1.jpg").astype(np.float32)
q_4_2=cv2.imread("black_hole/4/2.jpg").astype(np.float32)
q_4_3=cv2.imread("black_hole/4/3.jpg").astype(np.float32)
q_4_4=cv2.imread("black_hole/4/4.jpg").astype(np.float32)
q_4_5=cv2.imread("black_hole/4/5.jpg").astype(np.float32)

Q_1= (q_1_1 + q_1_2 + q_1_3 + q_1_4 + q_1_5) /5

Q_2= (q_2_1 + q_2_2 + q_2_3 + q_2_4 + q_2_5) /5

Q_3= (q_3_1 + q_3_2 + q_3_3 + q_3_4 + q_3_5) /5

Q_4= (q_4_1 + q_4_2 + q_4_3 + q_4_4 + q_4_5) /5

Q_1= Q_1.astype(np.uint8)

Q_2= Q_2.astype(np.uint8)

Q_3= Q_3.astype(np.uint8)

Q_4= Q_4.astype(np.uint8)

black_hole_U = np.concatenate((Q_1, Q_2), axis=1)
black_hole_D = np.concatenate((Q_3, Q_4), axis=1)
black_hole = np.concatenate((black_hole_U, black_hole_D), axis=0)

cv2.imshow("", black_hole)
cv2.waitKey()

cv2.imwrite("Black_Hole.jpg", black_hole)

