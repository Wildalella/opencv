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
cv.createTrackbar('H','isolatedColor', 0, 195, nothing)
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
    kernel = np.ones((5,5), np.uint8)
    dilated = cv.dilate(generatedMask, kernel, iterations=2)
    eroded = cv.erode(dilated, kernel, iterations=2)
    

    result = cv.bitwise_and(frame, frame, mask=generatedMask)
    
    

    #cv.imshow("frame", frame)
    #cv.imshow("binaryImg", eroded)
    
    #conert the frame from BGR to Gray
    # grayConverted = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow("frame", grayConverted)

    #Contours
    contours, hierarchy = cv.findContours(eroded, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for i in range(0, len(contours)):
         cv.drawContours(frame, contours, -1, (0, 255, 255), 2)
         
    
    if len(contours) > 0:
        # Find the largest contour
        c = max(contours, key=cv.contourArea)
        # Get the minimum enclosing circle
        ((x, y), radius) = cv.minEnclosingCircle(c)
        # Draw the circle if the radius is greater than a threshold
        if radius > 10:
            cv.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv.putText(frame, "Radius: {:.2f}".format(radius), (int(x) - 10, int(y) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)



    #if(len(contours)>0):
     #   area = cv.contourArea(contours[0])
      #  c = max(contours, key=cv.contourArea)
       # ((x,y), radius) = cv.drawContours

    cv.imshow("isolatedColor", result)
    cv.imshow("contours", frame)

    if cv.waitKey(1) == ord('q'):
        break
    elif cv.waitKey(1) == ord('s'):
        cv.imwrite('savedIm.png', frame)
        cv.imwrite('savedMask.png', generatedMask)
        cv.imwrite('savedResult.png', result)
cap.release()
cv.destroyAllWindows()