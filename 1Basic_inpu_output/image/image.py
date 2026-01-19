import cv2 
import os


#read images 
image_path = os.path.join('.','some_image.png')
img = cv2.imread(image_path)

#write images
image_paths = os.path.join('.','image.jpg')
Img = cv2.imwrite(image_paths, img)
#this will print the height, width and number of channels
#print(image.shape) #(7,15,3)


cv2.imshow('image',Img)
cv2.waitKey(0)