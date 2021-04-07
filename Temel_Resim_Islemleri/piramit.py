import cv2

resim = cv2.imread('cicek.jpg')
up = cv2.pyrUp(resim) # boyutu iki kat arttırır
down = cv2.pyrDown(resim) #boyutu iki kat küçültür.

cv2.imshow('orjinal', resim)
cv2.imshow('up', up)
cv2.imshow('down', down)

cv2.waitKey(0)
cv2.destroyWindow()