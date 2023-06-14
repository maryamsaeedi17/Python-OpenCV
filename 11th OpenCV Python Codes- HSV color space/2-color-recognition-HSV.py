#Red - Green - Blue - Yellow - Orange - Purple - White - Black
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

_, frame=cap.read()
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

rows, cols, _=frame.shape

while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    rows, cols, _=frame.shape
    #cv2.rectangle(frame,(300,240),(340,260),0,3)
    cv2.rectangle(frame,(230,200),(380,300),0,3)
    #pic=frame[200:300 , 230:380]
    pic=frame[240:260 , 300:340, 0:3]


    blurred = cv2.GaussianBlur(frame, (25,25), 0)
    frame[0:200, 0:640, 0:3] = blurred[0:200, 0:640, 0:3]
    frame[300:480, 0:640, 0:3] = blurred[300:480, 0:640, 0:3]
    frame[200:300, 0:228, 0:3] = blurred[200:300, 0:228, 0:3]
    frame[200:300, 380:640, 0:3] = blurred[200:300, 380:640, 0:3]

    h, s, v=cv2.split(pic)

    mean_h=np.mean(h)
    mean_s=np.mean(s)
    mean_v=np.mean(v)

    if (mean_h < 15 or mean_h > 170) and (mean_s > 30) and (mean_v > 115):
        color="Red"
    elif (80 < mean_h < 130) and (mean_s > 30 ) and (mean_v > 115):
        color="Blue"
    elif (35 < mean_h < 80) and (mean_s > 30) and (mean_v > 115):
        color="Green"
    elif (25 < mean_h  < 35) and (mean_v > 30) and (mean_v > 115):
        color="Yellow"
    elif (15 < mean_h < 25) and (mean_s > 30) and (mean_v > 115):
        color="Orange"
    elif (130 < mean_h < 170) and (mean_s > 30) and (mean_v > 115):
        color="Magenta"
    elif (mean_s < 30) and (mean_v > 115):
        color="White"
    elif mean_v<115:
        color="Black"

    cv2.putText(frame,color,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)

    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

