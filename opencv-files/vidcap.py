import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('D:\Code\otebooks\haar.xml')

cap = cv.VideoCapture(0)

while True:
    ret,frame = cap.read()
    grey = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    for x,y,w,h in faces:
        cv.rectangle(grey,(x,y),(x+w,y+h),(0,255,0),2)
        print(x,y,w,h)

    cv.imshow('result',grey)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()