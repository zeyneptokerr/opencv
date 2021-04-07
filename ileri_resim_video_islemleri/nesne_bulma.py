import cv2
import numpy as np

img_rgb = cv2.imread('resim.png')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2GRAY)

nesne = cv2.imread('resim1.png', 0)

w,h = nesne.shape[::-1] #son iki indeksi olan genişlik ve yüksekliği alır.

res = cv2.matchTemplate(img_gray, nesne, cv2.TM_CCOEFF_NORMED)
threshold = 0.8 #doğruluk payı

loc = np.where(res>threshold)#eşeletirmenin %80'inin büyük olanlarını loc değişkeninin içinde tut

for n in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, n, (n[0]+w, n[1]+h), (0,255,255), 2)

cv2.imshow('bulunan nesneler', img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()