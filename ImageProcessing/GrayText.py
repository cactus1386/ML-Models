import cv2

img = cv2.imread('./media/image/House.jpg')

img = cv2.resize(img, (500, 500))

font = cv2.FONT_HERSHEY_SIMPLEX
loc = (150, 30)
fontScale = 1
fontColor = (0, 0, 0)
cv2.putText(img, "Radin House", loc, font, fontScale,
            fontColor, lineType=2, thickness=3)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('Gray', gray)
cv2.imshow('House', img)
cv2.waitKey(0)
