import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgbg = fgbg.apply(frame)
    cv2.imshow('fgbg', fgbg)
    cv2.imshow('orjinal', frame)
    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()