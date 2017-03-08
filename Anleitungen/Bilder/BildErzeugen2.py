import numpy as np
import cv2

redPortion = np.full((480, 640), 255, np.uint8)
greenPortion = np.full((480, 640), 0, np.uint8)
bluePortion = np.full((480, 640), 0, np.uint8)

img = cv2.merge([bluePortion, greenPortion, redPortion]) #OpenCV benutzt BGR
cv2.imshow("farben", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
