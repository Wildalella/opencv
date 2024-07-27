import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

kernel = np.array([[-2.0, -2.0, 0.0],
                [ -2.0, 1.0, 1.0], 
                [0.0, 1.0, 2.0]])
    

while True:

    ret, img = capture.read()
   
    filtered = cv.filter2D(img, -1, kernel)

    cv.imshow("filtered img", filtered)

    if cv.waitKey(1) == ord('q'):
        break
    
cv.destroyAllWindows()
