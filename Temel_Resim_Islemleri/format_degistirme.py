import cv2
import numpy as np

def kaydet(path,image,jpg_kalite=None,png_compress=None):

    if jpg_kalite:
        cv2.imwrite(path,image,[int(cv2.IMWRITE_JPEG_QUALITY),jpg_kalite]) #jpg kalite

    elif png_compress:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION),png_compress]) #png sıkıştırma

    else:
        cv2.imwrite(path, image)

def main():
    impath = "cicek.png"
    img=cv2.imread(impath)

    cv2.imshow('Cicek',img)

    cikis_jpeg = "cikis2.jpg"
    kaydet(cikis_jpeg,img,jpg_kalite=85)

    cikis_png="cicek2PNG.png"
    kaydet(cikis_png,img,png_compress=4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()