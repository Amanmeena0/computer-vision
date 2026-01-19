import os

import cv2

img = cv2.imread(os.path.join('.','image.jpg'))

print(img.shape)

cropped_img = img[220:740, 220:840] #img[y_start:y_end, x_start:x_end]

print(cropped_img.shape)

cv2.imshow('img',img)
cv2.imshow('cropped_img',cropped_img)

cv2.waitKey(0)