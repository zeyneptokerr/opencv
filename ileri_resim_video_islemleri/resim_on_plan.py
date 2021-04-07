import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resim_on.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64) #arka plan
fgdModel = np.zeros((1,65), np.float64) #ön plan

dikdortgen = (400, 125, 500, 450) #yüzümüzün koordinatları

cv2.grabCut(img, mask, dikdortgen, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT) #5iterasyonla kontrol etsin,dikdörtgen bölgesine göre ön çıkarma modu
mask2 = np.where((mask==2) | (mask==0), 0,1).astype('uint8') #2 ve ya 0, 1 ve ya 4'de kullanılabilir.
img = img*mask2[:,:,np.newaxis] #dikdörtgen kısmını ön plana çıkarma durumu

plt.imshow(img)
plt.colorbar()
plt.show()