import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/Ravi B K/OneDrive/Desktop/miniproject/mp/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    col=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(
        col,
        scaleFactor= 1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
