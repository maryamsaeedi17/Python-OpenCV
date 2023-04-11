import numpy as np
import cv2

anooshe_image=cv2.imread("anoushe_ansari.jpg")
homa_image=cv2.imread("Homa_Sarshar.jpg")

anooshe_gray_image=cv2.cvtColor(anooshe_image, cv2.COLOR_BGR2GRAY)
homa_gray_image=cv2.cvtColor(homa_image, cv2.COLOR_BGR2GRAY)

#print(anooshe_gray_image.shape)

#print(homa_gray_image.shape)

homa_gray_image=homa_gray_image[:160 , :]
print(homa_gray_image.shape)

#homa_gray_image=cv2.resize(homa_gray_image, [anooshe_gray_image.shape[1], anooshe_gray_image.shape[0]])
anooshe_gray_image=cv2.resize(anooshe_gray_image, [homa_gray_image.shape[1], homa_gray_image.shape[0]])

anooshe_gray_image=anooshe_gray_image.astype(np.float32)
homa_gray_image=homa_gray_image.astype(np.float32)

morph1=anooshe_gray_image*3/4 + homa_gray_image*1/4
morph2=anooshe_gray_image*1/2 + homa_gray_image*1/2
morph3=anooshe_gray_image*1/4 + homa_gray_image*3/4

morph1=morph1.astype(np.uint8)
morph2=morph2.astype(np.uint8)
morph3=morph3.astype(np.uint8)

concatenated_image=np.concatenate((anooshe_gray_image, morph1, morph2, morph3, homa_gray_image), axis=1)

cv2.imshow("", concatenated_image)
cv2.waitKey()

cv2.imwrite("morph_result.jpg", concatenated_image)

