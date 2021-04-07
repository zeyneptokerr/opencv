import cv2

kamera = cv2.VideoCapture(0) # 0 webcam
#kamera = cv2.VideoCapture('smile.mp4') #harici video

'''
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,320) #genişlik 320
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,320) #yükseklik 320
'''

while True:
    ret, goruntu = kamera.read()
    griton = cv2.cvtColor(goruntu, cv2.COLOR_RGB2GRAY)
#   ret = kamera.set(3,600) #3 weight anlamına gelir
#   ret = kamera.set(4,600) #4 yükseklik anlamına gelir.
    cv2.imshow('Goruntu', goruntu)
    cv2.imshow('Gri Ton', griton)

    if cv2.waitKey(25) & 0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()