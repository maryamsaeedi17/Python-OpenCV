import cv2 

cap = cv2.VideoCapture(0)
_, frame= cap.read()
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
h, w= frame.shape

image= cv2.imread("Input\katy-perry.jpg", -1)
image= cv2.resize(image, (h, w))

while True :   
      
    cv2.imshow("funny filter" , image)   
    _, frame = cap.read()
    image[230:290 , 200:280] = frame[300:360 , 200:280]

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break