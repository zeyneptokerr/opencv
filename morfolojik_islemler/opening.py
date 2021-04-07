import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while(1):
    ret, frame = kamera.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dusuk_beyaz  = np.array([0,0,140])
    ust_beyaz  = np.array([256,60,256])

    mask= cv2.inRange(hsv, dusuk_beyaz, ust_beyaz)
    son_resim = cv2.bitwise_and(frame,frame,mask=mask)

    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1) #gürültüleri temizler.
    dilation = cv2.dilate(mask,kernel,iterations=1) #gürültüleri iyice arttırır.

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)
    #opening filtrenin içerisinde uymayan kısımları iyice belirginleştiriyor.
    #closing farklı gürültülü alanları iyice kapatır.

    cv2.imshow('orjinal', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
