import cv2
import numpy as np


def show(name, image):
    cv2.imshow(name, image)


img = cv2.imread('./media/car.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
show('gray image', gray)
cv2.imwrite('./media/grayCar.jpg', gray)

# Lowpass Filter
lowpass_kernel = np.ones((7, 7), dtype=np.float32) / 25
lowpass = cv2.filter2D(gray, -1, lowpass_kernel)
show('lowpass filter', lowpass)
cv2.imwrite('./media/lowpassCar.jpg', lowpass)


# edg kernel
x_edg_kernel = np.array([(1, 0, -1), (2, 0, -2), (1, 0, -1)])
y_edg_kernel = np.array([(1, 2, 1), (0, 0, 0), (-1, -2, -1)])
x_edg = cv2.filter2D(gray, -1, x_edg_kernel)
y_edg = cv2.filter2D(gray, -1, y_edg_kernel)

show('x edg', x_edg)
show('y edg', y_edg)
cv2.imwrite('./media/x_edgeCar.jpg', x_edg)
cv2.imwrite('./media/y_edgeCar.jpg', y_edg)


# High pass
highpass = np.abs(gray.astype('float') -
                  lowpass.astype('float')).astype('uint8')
show('Highpass', highpass)
cv2.imwrite("./media/highpassCar.jpg", highpass)


cv2.waitKey(0)
