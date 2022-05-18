import numpy as np
import cv2
 
image = cv2.imread("FotoBella.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original",image)
cv2.waitKey()
 
# Detección de borde de Laplace
lap = cv2.Laplacian(image,cv2.CV_64F)# Detección de borde de Laplace
lap = np.uint8(np.absolute(lap))## Ir al valor absoluto de vuelta
cv2.imshow("Laplaciano",lap)
cv2.waitKey()
