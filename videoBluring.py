import cv2 
video=cv2.VideoCapture(0)
video.set(3,400)
video.set(4,400)



while True:
    ret,frame=video.read()
    blur=cv2.GaussianBlur(frame,(5,5),0)
    blur1=cv2.medianBlur(frame,5,0)

    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
    cv2.imshow('image',frame)
    cv2.imshow('blur',blur)
    cv2.imshow('median',blur1)

video.release()
cv2.destroyAllWindows()