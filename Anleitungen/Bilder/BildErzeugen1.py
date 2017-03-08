import numpy as np
import cv2

#img = np.zeros((480, 640, 3), np.uint8) #Schwarz
img = np.full((480, 640, 3), 255, np.uint8) #Weiss

cv2.imshow("farben", img)
cv2.waitKey(0)
cv2.destroyAllWindows()