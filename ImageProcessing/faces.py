import cv2

face_cascade = cv2.CascadeClassifier(
    './media/models/haarcascade_frontalface_default.xml')

img = cv2.imread('./media/image/person.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 9)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
