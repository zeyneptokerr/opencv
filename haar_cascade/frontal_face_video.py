import cv2
import numpy as np

kamera = cv2.VideoCapture(0)
yuz_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while(1):
    ret, frame = kamera.read()

    griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(griton, 1.3, 4) #yüz kaç oranında skalasın = 1.3, min komşuluk = 4 yani kaç kere yüz var diye teyit etmesi.

    for (x, y, w, h) in yuzler:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)

    cv2.imshow('orjinal', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()