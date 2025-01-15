import cv2

img = cv2.imread('./media/image/football.jpg')

ball = img[393:460, 486:560, :]

img[393:460, 661:735, :] = ball

cv2.rectangle(img, (486, 393), (560, 460), (0, 0, 255), thickness=3)

cv2.imshow('football', img)
cv2.waitKey(0)

cv2.imwrite('./media/image/football_ball.jpg', img)
