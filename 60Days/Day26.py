import cv2 as cv
import numpy as np
#  Create two blank image
# uint8 -> unsigned integer of 8 bit -> 0 to 255
# 0 -> dark, 255 -> bright
img1 = np.zeros((300, 300), dtype = "uint8") 
img2 = np.zeros((300, 300), dtype = "uint8") 
# Draw a white rectangle on Image one
cv.rectangle(img1, (50, 50), (250, 250), 255, -1)
# Draw a white circle on image two
cv.circle(img2, (150, 150), 120, 255, -1)

cv.imshow("Rectangle", img1)
cv.imshow("Circle", img2)
# AND Operation
bit_and = cv.bitwise_and(img1, img2)
cv.imshow("AND", bit_and)
# OR Operation
bit_or = cv.bitwise_or(img1, img2)
cv.imshow("OR", bit_or)
# XOR Operation 
bit_xor = cv.bitwise_xor(img1, img2)
cv.imshow("XOR", bit_xor)
# NOT Operation 
bit_not = cv.bitwise_not(img1)
cv.imshow("NOT", bit_not)

cv.waitKey(0)
cv.destroyAllWindows()