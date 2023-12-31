import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")



while True:
    _,frame=cap.read()
    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame,1.4,4)


    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=img_gray[y:y+h,x:x+w]
        roi_rgb=frame[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(roi_gray)

        for(ex,ey,ew,eh)in eyes:
            cv2.rectangle(roi_rgb,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)

    cv2.imshow('image',frame)
    k=cv2.waitKey(1)


    if k==ord('q'):
        break
cap.realease()
cv2.destroyAllWindows()
