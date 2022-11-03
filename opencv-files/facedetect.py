import cv2 as cv 
import numpy

img  = cv.imread('D:\Code\otebooks\ddo.jpg')
haar_data = cv.CascadeClassifier('haar.xml')
haar_data.detectMultiScale(img)

faces_rect = haar_data.detectMultiScale(img, scaleFactor=1.1,minNeighbors=1)

while True:
    faces = haar_data.detectMultiScale(img)
    for x,y,w,h in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow('result',img)
    if cv.waitKey(0):
        break
cv.destroyAllWindows()