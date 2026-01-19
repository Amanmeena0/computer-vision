import os 
import cv2 

img = cv2.imread(os.path.join('.','image.jpg'))

resize_image = cv2.resize(img,(640,480))

print(img.shape)
print(resize_image.shape)

cv2.imshow('img',img)
cv2.imshow('resize_img',resize_image)
cv2.waitKey(0)