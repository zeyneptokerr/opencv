import numpy as np
import cv2

resim = cv2.imread('kose.png')
griton = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
griton = np.float32(griton)

koseler = cv2.goodFeaturesToTrack(griton,400,0.01,20)#100köşe, 20piksellik mesafelerle işleme alsın. 0.01 hassasiyeti

for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(resim,(x,y), 3,255,-1) #tespit ettiğimiz köşeleri daire içine alınmasını sağlıyoruz.

cv2.imshow('koseler',resim)
cv2.waitKey(0)
cv2.destroyAllWindows()