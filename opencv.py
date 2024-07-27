import cv2 as cv


img1 = cv.imread('butterfly.jpg')
img2 = cv.imread('flower.jpg')
height_im1 = img1.shape[0]
witdth_im1 = img1.shape[1]
height_im2 = img2.shape[0]
width_im2 = img2.shape[1]

min_height = min(height_im1, height_im2)
min_width = min( witdth_im1, width_im2)

cropped_im1 = img1[0:min_height, 0: min_width]
cropped_im2 = img2[0:min_height, 0:min_width]

addedimg = cv.add(cropped_im1, cropped_im2)
cv.imshow("added img1", addedimg)
cv.waitKey(0)
