import cv2

image=cv2.imread('aple.jpg')
himanshuimage=cv2.imread('himanshu.png')
himanshuimageR=cv2.resize(himanshuimage,(300,300))
image1=cv2.resize(image,(300,300))

_,thresh1=cv2.threshold(image1,150,255,cv2.THRESH_BINARY)
_,thresh2=cv2.threshold(image1,150,255,cv2.THRESH_BINARY_INV)
_,thresh3=cv2.threshold(himanshuimageR,150,255,cv2.THRESH_TOZERO)

cv2.imshow('Thres1',thresh1)
cv2.imshow('inv',thresh2)
cv2.imshow('small image',image1)
cv2.imshow('himanshurana',thresh3)
cv2.waitKey(0)



