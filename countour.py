import cv2

img = cv2.imread("infusing.jpg")
img = cv2.resize(img,(400,400))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,127,255,0)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Numbers of Contours:", str(len(contours)))

cv2.drawContours(img,contours,-1,(0,0,255),1)
cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()