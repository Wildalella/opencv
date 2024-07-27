import cv2 as cv
import numpy as np

savedIm = cv.imread('savedIm.png')
savedMask = cv.imread('savedMask.png')
savedMask = cv.cvtColor(savedMask, cv.COLOR_BGR2GRAY)
savedResult = cv.imread('savedResult.png')

contours, hierarchy = cv.findContours(savedMask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

img = cv.drawContours(savedIm, contours, 0, (0, 255,255), 2)

area = cv.contourArea(contours[0])
print(area)
#M = cv.moments(contours[0])

#cx = int(M['m10']/M['m00'])
#cy = int(M['m01']/M['m00'])

cv.imshow("contours", img)

cv.waitKey(0)
cv.destroyAllWindows()