import cv2 

video=cv2.VideoCapture(0)
video.set(3,500)
video.set(4,500)



while True:
    _,image=video.read()
    image1=cv2.flip(image,1)

    _,thresh1=cv2.threshold(image1,150,255,cv2.THRESH_BINARY)

    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
    cv2.imshow("runtime",thresh1)
video.release()
cv2.destroyAllWindows()
