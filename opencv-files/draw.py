import cv2 as cv
import numpy as np
#making blank images
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)
#img = cv.imread('D:\Code\my new files\puin.jpg')

#chaging properties in balnk images
#blank[:] = 0,255,0
#cv.imshow('bhlank',blank)

#drawing rectangles
#cv.rectangle(blank,(0,0),(250,2500),(0,253,0) ,thickness=cv.FILLED) #or we can use thickness = -1 to fill
#cv.imshow('rectangle',blank)
#cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,253,0) ,thickness=cv.FILLED)
#cv.imshow('rectangle',blank)

#drawing circle
#cv.circle(blank,(250,250),60,(0,255,255),thickness = -1)
#cv.imshow('circle',blank)

#darwing lines
#cv.line(blank,(0,0),(250,250),(0,0,255),thickness= 4)
#cv.imshow('line',blank)

#putting texts

cv.putText(blank,'hello wolrd',(250,250),cv.FONT_HERSHEY_DUPLEX,2.0,(0,234,234),thickness=4)
cv.imshow('text',blank)






cv.waitKey(0)