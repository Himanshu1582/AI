import cv2

img1=cv2.imread('images1.jpg')
img2=cv2.imread('images.png')
img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))

img3 = cv2.bitwise_and(img1,img2,mask=None)
img4 = cv2.bitwise_or(img1,img2, mask=None) 
img5 = cv2.bitwise_not(img1, mask=None) 

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img5',img5)

cv2.waitKey(0)