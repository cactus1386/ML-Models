import cv2
import numpy as np

path = './media/video/street.mp4'

capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(path))

bg = []
while True:
    ret, frame = capture.read()

    if frame is None:
        break

    bg.append(frame)

bg = np.array(bg)
bg = np.median(bg, axis=0)
bg = bg.astype('uint8')

cv2.imwrite('./media/image/BackgroundStreet.jpg', bg)
# cv2.imshow('Background', bg)

# cv2.waitKey(0)
capture.release()

capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(path))


while True:
    ret, frame = capture.read()

    resk = np.abs(frame.astype("float") - bg.astype("float")).astype('uint8')

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    resk = cv2.resize(resk, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('resk', resk)
    cv2.imshow('frame', frame)

    cv2.waitKey(1)
