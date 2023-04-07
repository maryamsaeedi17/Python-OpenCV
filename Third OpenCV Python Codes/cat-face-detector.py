import cv2

cat_image=cv2.imread("cats.jpeg")
cat_image=cv2.resize(cat_image, [800, 550])
cat_image_gray=cv2.cvtColor(cat_image, cv2.COLOR_BGR2GRAY)

cat_face_detector=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")

cat_faces=cat_face_detector.detectMultiScale(cat_image_gray, 1.3)

count=0
for cat_face in cat_faces:
    x, y, w, h = cat_face
    cv2.rectangle(cat_image, [x, y], [x+w, y+h], [137, 148, 0], 5)
    count+=1

print("Number of cats in the picture:", count)
cv2.imshow("", cat_image)
cv2.waitKey()

cv2.imwrite("cat_face_detected.jpg", cat_image)