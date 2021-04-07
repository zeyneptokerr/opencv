import cv2
import numpy as np
'''
resim = cv2.imread('cicek.png')
cv2.imshow('cicek', resim)

cv2.rectangle(resim,(200,70),(320,180),(255,0,0),2) #ilk sol üst köşe, ikinci sağ alt köşe, renk, kalınlık
cv2.imshow('dortgen', resim)
'''

resim = np.zeros((400,400,3),dtype='uint8')
cv2.rectangle(resim, (10,10),(390,210), (0,255,255),3)
cv2.imshow('siyah', resim)


cv2.waitKey(0)
cv2.destroyAllWindows()