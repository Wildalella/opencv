import cv2 as cv
import numpy as np

def nothing(x):
    pass

#create black image and window

img = np.zeros((300,512,3), np.uint8)
hasConverted = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.namedWindow('isolatedColor')

#Create a trackbar
cv.createTrackbar('H','isolatedColor', 0, 179, nothing )
cv.createTrackbar('S','isolatedColor', 0, 255, nothing )
cv.createTrackbar('V','isolatedColor', 0, 255, nothing )


#create a on/off switch
cv.createTrackbar('on/off', 'isolatedColor', 0, 1, nothing)

while(1):
    #show color, get the key press and if its esc, break
    cv.imshow('solatedColor', hasConverted)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# get posiotn of trackbar
    hPoint = cv.getTrackbarPos('H', 'isolatedColor')
    sPoint = cv.getTrackbarPos('S', 'isolatedColor')
    vPoint = cv.getTrackbarPos('V', 'isolatedColor')
    s = cv.getTrackbarPos('on/off', 'isolatedColor')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [hPoint, sPoint, vPoint, s]
cv.destroyAllWindows()





