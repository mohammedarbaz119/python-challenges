import cv2 as cv

#img = cv.imread('D:\Code\my new files\puin.jpg')
#cv.imshow("car",img)

def rescaleFrame(frame, scale = 0.75):
    #works for images videos and live videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation = cv.INTER_AREA )
def changeres(width,height):
    cap.set(3,width)
    cap.set(4,height)

cap = cv.VideoCapture("D:\Code\my new files\kuch.mp4")
while True:
    istrue, frame = cap.read()
    framer = rescaleFrame(frame,scale = 0.10)
    cv.imshow('vieo',frame)
    cv.imshow('vieor',framer)
    if cv.waitKey(20) and 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()


cv.waitKey(0)