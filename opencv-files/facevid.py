import cv2 as cv 
import numpy
haar_data = cv.CascadeClassifier('D:\Code\otebooks\haar.xml')
cap = cv.VideoCapture(0)
while True:
    flag, img = cap.read()
    if flag:
        faces = haar_data.detectMultiScale(img)
        for x,y,w,h in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
        cv.imshow('result',img)
        if cv.waitKey(2) == 27:
            break   
cap.release()    
cv.destroyAllWindows()
