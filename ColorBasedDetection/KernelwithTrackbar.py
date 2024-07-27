import cv2 as cv
import numpy as np

def nothing(x):
    pass

# window for trackbar
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

#Create a trackbar
cv.createTrackbar('Emboss','image', 0, 2, nothing )
cv.createTrackbar('Sharpen','image', 0, 255, nothing )
cv.createTrackbar('Blur','image', 0, 255, nothing )

#create a on/off switch
cv.createTrackbar('on/off', 'image', 0, 1, nothing)

capture = cv.VideoCapture(0)

emboss = np.array([[-2.0, -2.0, 0.0],
                [ -2.0, 1.0, 1.0], 
                [0.0, 1.0, 2.0]])




while True:

    ret, img = capture.read()
    filtered = cv.filter2D(img, -1, emboss)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("filtered img", filtered)


    #show color, get the key press and if its esc, break
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

# get posiotn of trackbar
    emboss = cv.getTrackbarPos('Emboss', 'image')
   # sharpen = cv.getTrackbarPos('G', 'image')
   # blur = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos('on/off', 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [emboss, s]

    
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()


   
    

    


