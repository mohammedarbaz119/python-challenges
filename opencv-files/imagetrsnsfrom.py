import cv2 as cv
import numpy

img = cv.imread('D:\Code\otebooks\puin.jpg')
cv.imshow('car',img)

#converting to greyscale
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grey)

#blurring iamge
blur =  cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)
#edge cascade
canny = cv.Canny(img,125,735)
cv.imshow('cannny',canny)

#dilation

dilated = cv.dilate(canny,(7,7),iterations=1)
cv.imshow('dilated',dilated)

#eroding

eroded = cv.erode(dilated,(5,5),iterations=1)
cv.imshow('eorded',eroded)

#resizing images

resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#croppping images
crop = img[40:200, 200:500]
cv.imshow('croppe',crop)


cv.waitKey(0)