import cv2

video=cv2.VideoCapture(0)
video.set(3,400)
video.set(4,400)

while True:
    ret,image1=video.read()
    image=cv2.flip(image1,1)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thresh=cv2.threshold(gray,127,255,0)

    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(image,contours,-1,(0,0,255),1)
    

    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
    cv2.imshow("runtime",image)
video.release()
cv2.destroyAllWindows()


