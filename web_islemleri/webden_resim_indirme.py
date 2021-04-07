import cv2
from skimage import io

adresler = [
    "https://upload.wikimedia.org/wikipedia/tr/2/2d/T%C3%BCrkiye_Cumhuriyeti_D%C3%BCzce_Valili%C4%9Fi_Kurumsal_Logosu.png",
    "https://upload.wikimedia.org/wikipedia/commons/9/9d/Wikipedia-logo-v2-en_5m_articles.png"
]

for adres in adresler:
    print("%s yukleniyor"%(adres))
    resim = io.imread(adres)
    cv2.imshow('BGR format', resim)
    cv2.imshow('RBG format', cv2.cvtColor(resim, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)