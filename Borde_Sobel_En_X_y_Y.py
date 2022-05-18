import numpy as np
import cv2
 
image = cv2.imread("FotoBella.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)
cv2.waitKey()
 
sobelX = cv2.Sobel(image,cv2.CV_64F,1,0)#x gradiente de dirección
sobelY = cv2.Sobel(image,cv2.CV_64F,0,1)#y gradiente de dirección
 
sobelX = np.uint8(np.absolute(sobelX))#x gradiente de dirección valor absoluto
sobelY = np.uint8(np.absolute(sobelY))#y valor absoluto del gradiente de dirección
 
sobelCombined = cv2.bitwise_or(sobelX,sobelY)#
cv2.imshow("Sobel X", sobelX)
cv2.waitKey()
cv2.imshow("Sobel Y", sobelY)
cv2.waitKey()
cv2.imshow("Sobel Combinada (XY)", sobelCombined)
cv2.waitKey()
