import cv2

face_cascade = cv2.CascadeClassifier(
    './media/models/haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 9)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Detected Faces', img)
    cv2.waitKey(30)

capture.release()
