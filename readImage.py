import cv2

image=cv2.imread('aple.jpg')
image1=cv2.resize(image,(600,600))
cv2.putText(image1,"Duplicate image",(200,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

cv2.imshow('window',image)
cv2.imshow('small image',image1)
cv2.waitKey(0)

cv2.destroyAllWindows()


