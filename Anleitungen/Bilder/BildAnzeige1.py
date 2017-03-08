import cv2

img = cv2.imread("farben.bmp", cv2.IMREAD_COLOR)
print(img) #Consolen Ausgabe
r,g,b = cv2.split(img)
img2 = cv2.merge([r,g,b])
cv2.namedWindow('farben', cv2.WINDOW_NORMAL)
cv2.imshow("farben", img)
cv2.resizeWindow('farben', 400, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()
