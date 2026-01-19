import cv2 
import os 

video_path = os.path.join('.','Memes_Download_For_Youtube_Video_Editing_Ghgccrr.mp4')

video = cv2.VideoCapture(video_path)
    
ret = True

while ret:
    
    ret, frame = video.read()

    cv2.imshow('frame', frame)
    cv2.waitKey(30)
video.release()
cv2.destroyAllWindows()