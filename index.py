#Owner Peyxw
import numpy as np
import cv2
  
# Calling Video
cap = cv2.VideoCapture('video.avi')

# Calling the XML File
car_cascade = cv2.CascadeClassifier('cars.xml')
  
# cycle starts
while True:
    # Reads Frames
    ret, frames = cap.read()
      
   
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
      
  
   
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
      
  
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
  
        
        cv2.imshow('video2', frames)
         
    # Esc tuşunun durmasını bekleyin
    if  cv2.waitKey(33) == 27:
        break
  

cv2.destroyAllWindows()
