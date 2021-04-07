import numpy as np
import cv2

'''
x = np.uint8([250])
y = np.uint8([10])

print(x+y) #ikisini toplayıp 255'e göre modunu alır
print(cv2.add(x,y)) '''

img = cv2.imread('opencv1.png')
img1 = cv2.imread('besiktas.png')

#toplam = cv2.add(img, img1)
toplam = cv2.addWeighted(img, 0.7, img1, 0.3,0)

cv2.imshow('toplam', toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()