#import time
import numpy as np
import cv2
# import tensorflow as tf
# from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
from TFLiteFaceAlignment import CoordinateAlignmentModel

fd = UltraLightFaceDetecion("weights/RFB-320.tflite", conf_threshold=0.88)
fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")

def facial_features_2x(landmarks, image):
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
    #doubled_feature=cv2.resize(result_fit, (0, 0), fx=2, fy=2)
    doubled_feature=cv2.resize(result_fit, (w*2, h*2))

    for i in range(h*2):
        for j in range(w*2):
            if doubled_feature[i][j][0] == 0 and doubled_feature[i][j][1] == 0 and doubled_feature[i][j][2] == 0:
                doubled_feature[i][j] = image[int(y-h//2)+i, int(x-w//2)+j]

    image[int(y-h//2):int(y-h//2)+h*2, int(x-w//2):int(x-w//2)+w*2]=doubled_feature

    return image

image=cv2.imread("Input\My-pic.jpg")

boxes, scores = fd.inference(image)

for pred in fa.get_landmarks(image, boxes):
    features_landmarks=[]


lip_landmarks=[52, 55, 56, 53, 59, 58, 61, 68, 67, 71, 63, 64]
right_eye_landmarks=[35, 36, 33, 37, 39, 42, 40, 41]
left_eye_landmarks=[89, 90, 87, 91, 93, 96, 94, 95]

image=facial_features_2x(lip_landmarks, image)
image=facial_features_2x(right_eye_landmarks, image)
image=facial_features_2x(left_eye_landmarks, image)


# cv2.imshow("lip", doubled_lip)
# cv2.imshow("R", doubled_right_eye)
# cv2.imshow("L", doubled_left_eye)
cv2.imshow("result", image)


cv2.waitKey()
cv2.imwrite("Output/My_exaggerated_pic.jpg", image)
