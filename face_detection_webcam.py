import cv2

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("D:\opencv_udemy/06_face_detection/frontalface.xml")

while True:

    _,frame=cap.read()
    frame=cv2.flip(frame,1)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv2.imshow("Video",frame)


    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()