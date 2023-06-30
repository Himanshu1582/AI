import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    _,frame=cap.read()
    faces=face_cascade.detectMultiScale(frame,1.4,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('image',frame)

    if cv2.waitKey(1)==ord('q'):
        break
cap.realease()
cv2.destroyAllWindows()
