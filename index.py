#Owner Peyxw
import numpy as np
import cv2
  
# video Çağırıyoruz
cap = cv2.VideoCapture('video1.avi')

# XML Dosyamızı Çağırıyoruz
car_cascade = cv2.CascadeClassifier('cars.xml')
  
# Arabalaı Gördüyse Döngü Başlar
while True:
    # Kareleri Okur
    ret, frames = cap.read()
      
    # her karenin gri ölçeğine dönüştür
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
      
  
    # Giriş görüntüsünde farklı boyutlardaki arabaları algılar
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
      
    # Her arabaya bir dikdörtgen çizmek için
    for (x,y,w,h) in cars:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
  
        # Çerçeveleri bir pencerede görüntüleme
        cv2.imshow('video2', frames)
         
    # Esc tuşunun durmasını bekleyin
    if  cv2.waitKey(33) == 27:
        break
  
# Ve Kodu Kapatın
cv2.destroyAllWindows()