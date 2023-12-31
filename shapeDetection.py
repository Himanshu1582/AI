from turtle import*
import cv2

img1=cv2.imread("shape2.png")
img=cv2.resize(img1,(1200,800))
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(approx)
        aspectratio=float(w)/h
        print(aspectratio)
        if aspectratio>=0.95 and aspectratio <=1.05:
            cv2.putText(img,"Square",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
        else:
            cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
            
    elif len(approx)==5:
        cv2.putText(img,"pentagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==7:
        cv2.putText(img,"Septagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==8:
        cv2.putText(img,"Octagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==9:
        cv2.putText(img,"Nanogon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    elif len(approx)==10:
        cv2.putText(img,"decagon",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    else:
        cv2.putText(img,"circle",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


