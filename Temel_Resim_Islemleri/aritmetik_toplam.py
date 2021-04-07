import numpy as np
import cv2

img1 = cv2.imread('cicek.jpg')
img2 = cv2.imread('opencv2.png')

satir, sutun, kanal = img2.shape
roi = img1[0:satir, 0:sutun]

im2gray = cv2.imread('opencv2.png',0)
#im2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB) #resmi griye çevirir
#cv2.imshow('im2gray', im2gray) 250,255
ret, mask = cv2.threshold(im2gray, 250, 255, cv2.THRESH_BINARY)
mas_inv = cv2.bitwise_not(mask) #maskın tersini aldık
#cv2.imshow('mask', mask)
#cv2.imshow('mas_inv', mas_inv)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask) #logonun arkasına çiçek arkaplanı yaptık
#cv2.imshow('img1_bg', img1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask=mas_inv) #logonun arkasını siyah yaptık
cv2.imshow('img2_fg', img2_fg)


son_resim = cv2.add(img1_bg, img2_fg)
img1[0:satir, 0:sutun] = son_resim
cv2.imshow('son_resim', son_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()