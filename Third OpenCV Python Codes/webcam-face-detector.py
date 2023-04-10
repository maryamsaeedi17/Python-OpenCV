import cv2
import numpy as np

def checkered_face(image):
    faces = face_detector.detectMultiScale(image)
    for face in faces:
        x, y, w, h = face
        face_image = image[y:y+h, x:x+w]
        face_image_small = cv2.resize(face_image, [10, 10])
        face_image_big = cv2.resize(face_image_small, [w, h], interpolation=cv2.INTER_NEAREST)
        image[y:y+h, x:x+w] = face_image_big

    return image

def sticker_on_face(faces, image):
    for face in faces:
        x, y, w, h = face
        sticker = cv2.resize(smile_sticker,[w,h])
        for i in range(h):
            for j in range(w):
                if sticker[i][j][0] == 0 and sticker[i][j][1] == 0 and sticker[i][j][2] == 0:
                    sticker[i][j] = image[y+i,x+j]
        frame[y:y+h, x:x+w] = sticker
    return image

def sticker_on_lip_eye(lips, eyes, image):
    for lip in lips:
            x,y,w,h = lip
            sticker = cv2.resize(lip_sticker,[w,h])
            for i in range(h):
                for j in range(w):
                    if sticker[i][j][0] == sticker[i][j][1] == sticker[i][j][2] ==0 or sticker[i][j][0] == sticker[i][j][1] == sticker[i][j][2] ==255:
                        sticker[i][j] = image[y+i,x+j]
            image[y:y+h,x:x+w] = sticker
    
    w_g=1
    h_g=1
    x_g=600
    y_g=400
    for eye in eyes:
        x, y, w, h = eye
        w_g += w
        if h > h_g:
            h_g=h
        if x < x_g:
            x_g=x
        if y < y_g:
            y_g=y
        

    sticker_2 = cv2.resize(glasses_sticker,[w_g, h_g])
    for i in range(h_g):
        for j in range(w_g):
            if sticker_2[i][j][0] == sticker_2[i][j][1] == sticker_2[i][j][2] ==0:
                sticker_2[i][j] = image[y_g+i,x_g+j]
    image[y_g:y_g+h_g,x_g:x_g+w_g] = sticker_2


    return image



def symmetry_image(image):
    col = image.shape[1]
    flipVertical = cv2.flip(image[:,:col//2], 1)
    image[:,col//2:] = flipVertical

    return image



cap=cv2.VideoCapture(0)
smile_sticker=cv2.imread("smile-sticker.png")
lip_sticker=cv2.imread("lip.png")
glasses_sticker=cv2.imread("glasses2.png")

#print(smile_sticker.shape)


face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
eye_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
lip_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

while True:
    _, frame = cap.read()
    frame_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=face_detector.detectMultiScale(frame_gray, 1.3)
    lips = lip_detector.detectMultiScale(frame_gray, 1.3, minSize=(20, 50), maxSize=(70,200))
    
    eyes = eye_detector.detectMultiScale(frame_gray, 1.3, minSize=(50, 60))




    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

    elif cv2.waitKey(25) & 0xFF==ord("1"):
        frame=checkered_face(frame)

    elif cv2.waitKey(25) & 0xFF==ord("2"):
        frame=sticker_on_face(faces, frame)

    elif cv2.waitKey(25) & 0xFF==ord("3"):
        frame=sticker_on_lip_eye(lips, eyes, frame)

    elif cv2.waitKey(25) & 0xFF==ord("4"):
        frame=symmetry_image(frame)

    cv2.imshow("", frame)