#import time
import numpy as np
import cv2
# import tensorflow as tf
# from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

def rotate_facial_features(landmarks, image):
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
    rotated_feature=cv2.flip(result_fit, 0)

    for i in range(h):
        for j in range(w):
            if rotated_feature[i][j][0] == 0 and rotated_feature[i][j][1] == 0 and rotated_feature[i][j][2] == 0:
                rotated_feature[i][j] = image[y+i, x+j]

    image[y:y+h, x:x+w]=rotated_feature

    return image

image=cv2.imread("Input\My-pic.jpg")

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    features_landmarks=[]


lip_landmarks=[52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
right_eye_landmarks=[35, 36, 33, 37, 39, 42, 40, 41]
left_eye_landmarks=[89, 90, 87, 91, 93, 96, 94, 95]

image=rotate_facial_features(lip_landmarks, image)
image=rotate_facial_features(right_eye_landmarks, image)
image=rotate_facial_features(left_eye_landmarks, image)

rotated_image=cv2.flip(image, 0)

# cv2.imshow("lip", rotated_lip)
# cv2.imshow("R", rotated_right_eye)
# cv2.imshow("L", rotated_left_eye)
cv2.imshow("result", image)


cv2.waitKey()
cv2.imwrite("Output/My_wrong_pic.jpg", rotated_image)
