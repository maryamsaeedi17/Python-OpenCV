import cv2
import numpy as np

cap=cv2.VideoCapture(0)

_, frame=cap.read()
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

rows, cols=frame.shape

#print(frame.shape)

writer = cv2.VideoWriter("color_detector.mp4", cv2.VideoWriter_fourcc(*'XIVD'), 30, (cols, rows))

while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rows, cols=frame.shape
    #cv2.rectangle(frame,(300,240),(340,260),0,3)
    cv2.rectangle(frame,(230,200),(380,300),0,3)
    #pic=frame[200:300 , 230:380]
    pic=frame[240:260 , 300:340]


    blurred = cv2.GaussianBlur(frame, (25,25), 0)
    frame[0:200, 0:640] = blurred[0:200, 0:640]
    frame[300:480, 0:640] = blurred[300:480, 0:640]
    frame[200:300, 0:228] = blurred[200:300, 0:228]
    frame[200:300, 380:640] = blurred[200:300, 380:640]

    mean=np.mean(pic)
    if mean>170:
        color="White"
    elif 85<=mean<=170:
        color="Gray"
    elif mean<85:
        color="Black"

    cv2.putText(frame,color,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)

    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    writer.write(frame)
    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

writer.release()