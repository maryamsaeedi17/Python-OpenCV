#Red - Green - Blue - Yellow - Orange - Purple - White - Black
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

_, frame=cap.read()
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

rows, cols, _=frame.shape

#print(frame.shape)

#writer = cv2.VideoWriter("color_detector.mp4", cv2.VideoWriter_fourcc(*'XIVD'), 30, (cols, rows))

while True:
    _,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
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

    mean_r=np.mean(pic[:,:,0])
    mean_g=np.mean(pic[:,:,1])
    mean_b=np.mean(pic[:,:,2])

    if (mean_r>170) & (mean_g<85) & (mean_b<85):
        color="Red"
    elif (mean_r<85) & (mean_g<85) & (mean_b>170):
        color="Blue"
    elif (mean_r<85) & (mean_g>170) & (mean_b<85):
        color="Green"
    elif (mean_r>170) & (mean_g>170) & (mean_b<85):
        color="Yellow"
    elif (mean_r>170) & (85<mean_g<170) & (mean_b<85):
        color="Orange"
    elif (mean_r>170) & (mean_g<85) & (mean_b>170):
        color="Magenta"
    elif (mean_r>170) & (mean_g>170) & (mean_b>170):
        color="White"
    elif (mean_r<85) & (mean_g<85) & (mean_b<85):
        color="Black"

    cv2.putText(frame,color,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,0,2)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #writer.write(frame)
    cv2.imshow("",frame)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

#writer.release()