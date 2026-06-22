# Gradient -> refers to the rate of change in pixel intensity (brightness) between neighboring pixels.
# Suppose a row of pixels has these intensity values:[10   12   15   18   200   205] Between:18 → 200, there is a huge change. That means there's likely an edge.
# An edge is a boundary where there is a sudden change in brightness, color, or intensity between neighboring pixels.
# Sobel method -> a gradient-based method that helps detect edges by measuring changes in pixel brightness.
# Sobel calculates gradients in two directions:
# 1. X-direction (Vertical edges)
# 2. Y-direction (Horizontal edges)

import cv2 as cv
import numpy as np
img = cv.imread(r"Project1\Image\building.webp")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)


#laplacian method -> an edge detection technique that finds edges by calculating the second derivative of an image.
# lap = cv.Laplacian(gray, cv.CV_64F)   # second derivative -> +ve and -ve
# lap = np.uint8(np.absolute(lap))
# cv.imshow("Laplacian Image", lap)




#Sobel Method
# sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
# sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
# cv.imshow("Sobel-X", sobel_x)
# cv.imshow("Sobel-Y", sobel_y)
# combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
# combined_sobel = np.uint8(np.absolute(combined_sobel))
# cv.imshow("Combined Sobel Image", combined_sobel)





#canny method 
edges = cv.Canny(gray, threshold1 = 100, threshold2 = 500)
cv.imshow("Canny Image", edges)

cv.waitKey(0) 