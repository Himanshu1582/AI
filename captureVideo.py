import cv2 

video=cv2.VideoCapture(0)
video.set(3,500)
video.set(4,500)

while True:
    _,image=video.read()
    image=cv2.flip(image,1)

    if cv2.waitKey(1) & 0xFF==ord('a'):
        break
    cv2.imshow("runtime",image)
video.release()
cv2.destroyAllWindows()
