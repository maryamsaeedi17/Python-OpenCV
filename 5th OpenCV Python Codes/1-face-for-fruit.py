#import time
import numpy as np
import cv2
# import tensorflow as tf
# from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

def facial_features_extraction(landmarks, pred):
    features_landmarks=[]
    for i in landmarks:
        features_landmarks.append(pred[i])
    features_landmarks=np.array(features_landmarks, dtype=int)
    #print(features_landmarks)

    x, y, w, h=cv2.boundingRect(features_landmarks)
    mask=np.zeros(image.shape, dtype=np.uint8)
    cv2.drawContours(mask, [features_landmarks], -1, (255, 255, 255), -1)
    mask=mask // 255

    result=image*mask
    result_fit=result[y:y+h, x:x+w]

    return result_fit

image=cv2.imread("Input\Audrey_Hepburn.jpg")
color=(125, 255, 125)

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    # for i, p in enumerate(np.round(pred).astype(np.int)):
    #     cv2.circle(image, tuple(p), 2, color, -1)
    #     cv2.putText(image, str(i), tuple(p), cv2.FONT_HERSHEY_SIMPLEX , 0.3, (0, 0, 255))
    features_landmarks=[]
#pred=fa.get_landmarks(image, boxes)

lip_landmarks=[52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
#right_eye_landmarks=[35, 36, 33, 37, 39, 75, 42, 40, 41]
right_eye_landmarks=[35, 36, 33, 37, 39, 42, 40, 41]
#left_eye_landmarks=[81, 89, 90, 87, 91, 93, 96, 94, 95]
left_eye_landmarks=[89, 90, 87, 91, 93, 96, 94, 95]

fit_lip=facial_features_extraction(lip_landmarks, pred)
fit_right_eye=facial_features_extraction(right_eye_landmarks, pred)
fit_left_eye=facial_features_extraction(left_eye_landmarks, pred)

fit_lip=cv2.resize(fit_lip, [75, 28])
fit_right_eye=cv2.resize(fit_right_eye, [45, 19])
fit_left_eye=cv2.resize(fit_left_eye, [45, 20])

#cv2.imwrite("Output\Audrey_landmarks.jpg", image)
# cv2.imwrite("Output/Audrey_lip.jpg", fit_lip)
# cv2.imwrite("Output/Audrey_right_eye.jpg", fit_right_eye)
# cv2.imwrite("Output/Audrey_left_eye.jpg", fit_left_eye)

red_apple=cv2.imread("Input/red_apple.png")

#cv2.rectangle(red_apple, (60, 100), (166,175), (0, 0, 0), 1 )

# print(red_apple.shape) #(223, 226)

mask=np.zeros([75, 106, 3])
mask[0:19, 0:45 , 0:3]=fit_right_eye
mask[0:20, 60:105]=fit_left_eye
mask[46:74, 16:91]=fit_lip

x, y, w, h = [60, 100, 106, 75]
for i in range(h):
    for j in range(w):
        if mask[i][j][0] == 0 and mask[i][j][1] == 0 and mask[i][j][2] == 0:
            mask[i][j] = red_apple[y+i,x+j]
red_apple[y:y+h, x:x+w] = mask

cv2.imshow("", mask)
cv2.imshow("apple", red_apple)
cv2.waitKey()
#cv2.imwrite("Output/test_mask.jpg", mask)
cv2.imwrite("Output/face_for_red_apple.jpg", red_apple)