import pafy
import cv2

url = 'https://www.youtube.com/watch?v=T01z8vZEIM8'
vPaffy = pafy.new(url)
play = vPaffy.getbest(preftype="webm")

kamera = cv2.VideoCapture(play.url)
while True:
    ret, video = kamera.read()
    griton = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('video', video)
    cv2.imshow('griton', griton)
    if cv2.watershed(20) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()