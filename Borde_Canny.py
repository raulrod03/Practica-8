import numpy as np
import cv2
 
image = cv2.imread("FotoBella.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)#Convertir imagen a imagen en escala de grises
cv2.imshow("Image",image)#Mostrar imagen
cv2.waitKey()
 
canny = cv2.Canny(image,30,150)
cv2.imshow("Canny",canny)
cv2.waitKey()
