import cv2
import numpy as np

TV_image=cv2.imread("TV-img.jpg")
TV_image=cv2.cvtColor(TV_image, cv2.COLOR_BGR2GRAY)

rows, cols=TV_image.shape

writer=cv2.VideoWriter("TV_noise.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

while True:
    TV_image=cv2.imread("TV-img.jpg")
    TV_image=cv2.cvtColor(TV_image, cv2.COLOR_BGR2GRAY)
    TV_noise=np.random.random((328, 577))*255
    TV_noise=np.array(TV_noise, dtype=np.uint8)
    TV_image[30:358, 27:604]=TV_noise
    TV_image=cv2.cvtColor(TV_image, cv2.COLOR_GRAY2BGR)
    writer.write(TV_image)
    cv2.imshow("", TV_image)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

writer.release()

    
#print(TV_image.shape)
cv2.rectangle(TV_image, (27,30), (604,358), 200)

#cv2.imshow("", TV_image)

#cv2.waitKey()


#writer=cv2.VideoWriter("TV_noise.mp4", cv2.VideoWriter_fourcc(*'XVID'), 30, (cols, rows))

# while True:
#     TV_image=cv2.imread("TV.png")
#     TV_image=cv2.cvtColor(TV_image, cv2.COLOR_BGR2GRAY)
#     TV_noise=np.random.random((87, 117))*255
#     TV_noise=np.array(TV_noise, dtype=np.uint8)
#     TV_image[18:105, 19:136]=TV_noise
#     TV_image=cv2.cvtColor(TV_image, cv2.COLOR_GRAY2BGR)
#     writer.write(TV_image)
#     cv2.imshow("", TV_image)
#     if cv2.waitKey(25) & 0xFF==ord("q"):
#         break

# writer.release()

