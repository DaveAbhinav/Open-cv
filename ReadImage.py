import cv2
img = cv2.imread("butterfly.jpg")
cv2.imshow("display image", img)
print(img)
#cv2.waitKey(0)
grayimage=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale", grayimage)
print(grayimage)
cv2.waitKey(0)