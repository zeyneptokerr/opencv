import numpy as np
import cv2

resim = np.zeros((400,400,3),dtype='uint8')
cv2.line(resim, (10,10),(390,210), (0,255,255),3)

cv2.circle(resim,(200,350),25,(140,0,4),3) #çember çizimi, merkez, çap

cv2.putText(resim,'Zeynep', (5,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,25),2,cv2.LINE_4) #koordinat olarak sol alt köşe baz alınır.

cv2.imshow('siyah', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()