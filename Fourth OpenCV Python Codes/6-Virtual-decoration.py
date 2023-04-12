import numpy as np
import cv2

room_img=cv2.imread("vd1.jpg")
floor_img=cv2.imread("vd2.jpg")
mask_img=cv2.imread("vd3.jpg")

#print(room_img.shape)

room_img=cv2.resize(room_img, [698, 632])
floor_img=cv2.resize(floor_img, [698, 632])
mask_img=cv2.resize(mask_img, [698, 632])

mask_img=mask_img / 255

inv_mask=255-mask_img
inv_mask=inv_mask / 255

masked_floor= floor_img * mask_img
masked_room= room_img * inv_mask

floored_room= masked_floor + masked_room

cv2.imshow("", floored_room)
cv2.waitKey()

cv2.imwrite("floored_room.jpg", floored_room)