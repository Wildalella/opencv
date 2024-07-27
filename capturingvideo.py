import cv2 as cv
import numpy as np

#makes object for camera
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()

while True:
    #capure a frame
    ret, frame = cap.read()

    #if frame is read correctly, ret should be true
    if not ret:
        print('Cant recieve frame, Exiting..')
        break

#convert color to gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)

    if cv.waitKey(1) ==  ord('q'):
        break

#ALWAYS RELASE YOUR VIDEO CAPTURE OBJECT

cap.release()

cv.destroyAllWindows()