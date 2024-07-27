import cv2 as cv
import numpy as np
def nothing(x):
    pass

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera no work")
    exit()
img = np.zeros((640, 480, 3), np.uint8)
cv.namedWindow('isolatedColor')
cv.createTrackbar('H','isolatedColor', 0, 179, nothing)
cv.createTrackbar('S','isolatedColor', 0, 255, nothing)
cv.createTrackbar('V','isolatedColor', 0, 255, nothing)

while True:
    #capture a frame
    ret, frame = cap.read()
    if not ret:
        print("couldn't get a frame")
        break
    #convert our frame from BGR to HSV
    hsvConverted = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hPoint = cv.getTrackbarPos('H', 'isolatedColor')
    sPoint = cv.getTrackbarPos('S', 'isolatedColor')
    vPoint = cv.getTrackbarPos('V', 'isolatedColor')

    hLower = hPoint - 10
    hUpper = hPoint + 10
    sLower = sPoint - 50
    sUpper = sPoint + 50
    vLower = vPoint - 50
    vUpper = vPoint + 50
    if hLower < 0: hLower = 0
    if hUpper > 179: hUpper = 179
    if sLower < 0: sLower = 0
    if sUpper > 255: sUpper = 255
    if vLower < 0: vLower = 0
    if vUpper > 255: vUpper = 255

    #define boundaries for what we consider to be color
    lower = np.array([hLower,sLower,vLower])
    upper = np.array([hUpper,sUpper,vUpper])

    generatedMask = cv.inRange(hsvConverted, lower, upper)
    kernel = np.ones((5,5))

    result = cv.bitwise_and(frame, frame, mask=generatedMask)
    
    

    cv.imshow("frame", frame)
    cv.imshow("mask", generatedMask)
    cv.imshow("isolatedColor", result)
    #conert the frame from BGR to Gray
    # grayConverted = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow("frame", grayConverted)
    if cv.waitKey(1) == ord('q'):
        break
    elif cv.waitKey(1) == ord('s'):
        cv.imwrite('savedIm.png', frame)
        cv.imwrite('savedMask.png', generatedMask)
        cv.imwrite('savedResult.png', result)
cap.release()
cv.destroyAllWindows()