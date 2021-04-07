import cv2
img=cv2.imread('saat.jpg')

cv2.imshow('saat', img)
print(img[80,80]) #80,80 noktasının RGB değerleri
img[80,80] = [255,255,255] #80,80 noktasının değerini değiştirebiliyoruz.

bolge = img[20:250,100:300] #saat bölgesini kırptık
#img[20:250,100:300] = [255,0,255] #bölgeyi beyaz yapar
#img[0:240,0:210] = bolge #bölgeyi kopyalayıp belirtilen alana yapıştırır.

cv2.rectangle(img, (130,20), (250,150),(0,255,255),2) #saatin etrafına çerçeve çizdik.

cv2.imshow('saat',img)
cv2.imshow('saat2', bolge)
cv2.waitKey(0)
cv2.destroyAllWindows()