import cv2 as cv
import numpy as np

# Define the specific HSV color range you want to detect
hLower = 35  
hUpper = 35  
sLower = 77
sUpper = 89
vLower = 205
vUpper = 222

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working")
    exit()

img = np.zeros((640, 480, 3), np.uint8)

while True:
    # Capture a frame
    ret, frame = cap.read()
    if not ret:
        print("Couldn't get a frame")
        break


 # Define boundaries for the specific color
    lower = np.array([hLower, sLower, vLower])
    upper = np.array([hUpper, sUpper, vUpper])

    # Convert the frame from BGR to HSV
    hsvConverted = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Generate mask and perform morphological operations
    generatedMask = cv.inRange(hsvConverted, lower, upper)
    kernel = np.ones((5, 5), np.uint8)
    dilated = cv.dilate(generatedMask, kernel, iterations=2)
    eroded = cv.erode(dilated, kernel, iterations=2)



    # Apply mask to the original frame
    result = cv.bitwise_and(frame, frame, mask=generatedMask)

    # Find contours
    contours, hierarchy = cv.findContours(eroded, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for i in range(0, len(contours)):
         cv.drawContours(frame, contours, -1, (0, 255, 255), 2)
         
    # Draw all contours on the frame
    cv.drawContours(frame, contours, -1, (0, 255, 255), 2)

    # Show the frames
    cv.imshow("isolatedColor", result)
    cv.imshow("contours", frame)

    # Break loop on 'q' key press, save images on 's' key press
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite('savedIm.png', frame)
        cv.imwrite('savedMask.png', generatedMask)
        cv.imwrite('savedResult.png', result)

# Release resources
cap.release()
cv.destroyAllWindows()