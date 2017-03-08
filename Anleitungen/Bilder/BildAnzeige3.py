import cv2

img = cv2.imread("farben_grau.bmp", cv2.IMREAD_UNCHANGED)
print(img) #Consolen Ausgabe
r,g,b = cv2.split(img) #Exception!!!
cv2.namedWindow('farben', cv2.WINDOW_NORMAL)
cv2.imshow("farben", img)
cv2.resizeWindow('farben', 400, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()