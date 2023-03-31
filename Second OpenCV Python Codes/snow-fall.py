import numpy as np
import random
import cv2

image=cv2.imread("snowy lanscape.jpg")
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rows, cols=image.shape

writer=cv2.VideoWriter("snow_fall.mp4", cv2.VideoWriter_fourcc(*'XVID'), 10, (cols, rows))


while True:
    image=cv2.imread("snowy lanscape.jpg")
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    x = np.random.randint(0, image.shape[1], size=1000)
    y = np.random.randint(0, image.shape[0], size=1000)

    for i in range(len(x)):
        cv2.circle(image, (x[i], y[i]), random.randint(0,3), (255, 255), -1)

    noise = np.zeros_like(image)
    cv2.randn(noise, (0), (50))
    img = cv2.add(image, noise)

    image=cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    writer.write(image)

    cv2.imshow("", image)
    if cv2.waitKey(60) & 0xFF==ord("q"):
        break


writer.release()
