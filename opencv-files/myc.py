import cv2 as cv 
import numpy
cap = cv.VideoCapture("D:\Code\my new files\kuch.mp4")
while True:
    istrue, frame = cap.read()
    cv.imshow('vieo',frame)
    if cv.waitKey(20) and 0xFF==ord('s'):
        break
cap.release()
cv.destroyAllWindows()