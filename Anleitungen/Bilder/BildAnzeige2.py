import cv2

img = cv2.imread("farben.bmp", cv2.IMREAD_GRAYSCALE)
print(img) #Consolen Ausgabe
g = cv2.split(img)
cv2.namedWindow('farben', cv2.WINDOW_NORMAL)
cv2.imshow("farben", img)
cv2.resizeWindow('farben', 400, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()