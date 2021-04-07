import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
path = "yuz_verileri"
cam = cv2.VideoCapture(0)

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    for (x,y,w,h) in faces:
        tahminEdilenKisi, conf = recognizer.predict(gray[y:y+h, x:x+w])
        cv2.rectangle(im, (x-10, y-10), (x+w+10, y+h+10), (255,0,0), 2)
        if (tahminEdilenKisi == 1):
            tahminEdilenKisi = "Zeynep Toker"
        elif (tahminEdilenKisi == 2):
            tahminEdilenKisi = "Sis"
        elif (tahminEdilenKisi == 3):
            tahminEdilenKisi = "Anniş"
        elif (tahminEdilenKisi == 4):
            tahminEdilenKisi = "Bro"
        else:
            tahminEdilenKisi = "bilinmeyen kişi"

        fontFace = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontColor = (255,255,255)
        cv2.putText(im, str(tahminEdilenKisi), (x,y+h), fontFace, fontScale, fontColor)
        cv2.imshow("resim", im)
        cv2.waitKey(10)

