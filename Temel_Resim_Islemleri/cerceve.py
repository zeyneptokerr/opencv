import cv2
import numpy as np
from matplotlib import pyplot as plt

mavi = [255,0,0]

img=cv2.imread('opencv.png')

constant = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT, value=mavi)
replicate = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_REPLICATE)
wrap = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_WRAP)

plt.subplot(231),plt.imshow(img, 'gray'),plt.title('orjinal')
plt.subplot(232),plt.imshow(replicate, 'gray'),plt.title('replicate')
plt.subplot(233),plt.imshow(constant, 'gray'),plt.title('constant')
plt.subplot(234),plt.imshow(wrap, 'gray'),plt.title('wrap')

plt.show()

#cv2.imshow('orjinal', img)
#cv2.imshow('constant', constant)
cv2.waitKey(0)
cv2.destroyWindow()