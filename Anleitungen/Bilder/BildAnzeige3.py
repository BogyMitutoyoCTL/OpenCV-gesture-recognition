import cv2

img = cv2.imread("farben_grau.bmp", cv2.IMREAD_UNCHANGED)
r,g,b = cv2.split(img) #Exception!!!
cv2.imshow("farben", img)
cv2.waitKey(0)
cv2.destroyAllWindows()