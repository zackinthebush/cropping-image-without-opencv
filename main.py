import numpy as np
import cv2

#fanction recadrage
def recadrage32(image):
    resultat = image.copy()
    for x in range(image.shape[0]//32):
        for y in range(image.shape[1]//32):
            a = np.amin(image[x*32:(x+1)*32,y*32:(y+1)*32])
            b = np.amax(image[x*32:(x+1)*32,y*32:(y+1)*32])
            for i in range(image[x*32:(x+1)*32,y*32:(y+1)*32].shape[0]):
                for j in range(image[x*32:(x+1)*32,y*32:(y+1)*32].shape[1]):
            #test pour verifier l'image en gris ou en couleur
                    if len(resultat.shape)<3 :
                        resultat[i, j] = (255 / (b - a)) * (resultat[i, j] - a)
                    else :
                        for k in range(resultat.shape[2]):
                            resultat[i, j, k] = (255 / (b - a)) * (resultat[i, j, k] - a)
    print(resultat)
    cv2.imwrite("result.jpg", resultat)



image = cv2.imread(r"download.jpg", 1)
recadrage32(image)
cv2.imread("result.jpg")