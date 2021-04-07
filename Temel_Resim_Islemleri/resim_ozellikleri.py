import cv2
import numpy as np

#img = cv2.imread('cicek.jpg', 0) #gri resim yapar
img = cv2.imread('cicek.jpg')
#print(str(img.item(100,100,2))) # 0=mavi, 1=yeşil, 2=kırmızı
#üstteki kod 100-100 koordinatlarındaki kırmızı rengin piksel değerini verir bize.
#img.itemset((100,100,1),255) #100-100 koordinatlardaki yeşil pikselini 255 yapar.

#print(str(img.shape)) #yüksekliğini, genişliğini ve renkli resim olup olmadığını verir.

#print(str(img.size)) #piksel sayısını verir.

#print(img.dtype) #tipini görme

#alttaki kod resmin belirtilen kısımlarına göre kırpma işlemi yapar.
#ROI = img[310:486,272:400] #ilki y koordinatlarına göre ikincisi x bileşenlerine göre
#cv2.imshow('roi',ROI)

#img[310:486, 172:300] = ROI #kırpılan kısım resmin üzerine yapıştırıldı.

img[:,:,2] = 0 #resmin kırmızı bileşenlerini sıfırlar

cv2.imshow('resim', img)
cv2.waitKey(0)
cv2.destroyWindow()


