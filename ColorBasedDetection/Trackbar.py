import cv2 as cv
import numpy as np

def nothing(x):
    pass

#create black image and window

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

#Create a trackbar
cv.createTrackbar('R','image', 0, 255, nothing )
cv.createTrackbar('G','image', 0, 255, nothing )
cv.createTrackbar('B','image', 0, 255, nothing )

#create a on/off switch
cv.createTrackbar('on/off', 'image', 0, 1, nothing)

while(1):
    #show color, get the key press and if its esc, break
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# get posiotn of trackbar
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos('on/off', 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
cv.destroyAllWindows()





