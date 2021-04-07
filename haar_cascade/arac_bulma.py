import cv2

cascade_src = 'cars.xml'
video_src = 'car.mp4'

cap = cv2.VideoCapture(video_src)
cars_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    araclar = cars_cascade.detectMultiScale(gray, 1.2, 3)

    for (x,y,w,h) in araclar:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow('araclar', img)
    if cv2.waitKey(25) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
