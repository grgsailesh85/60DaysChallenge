import cv2 as cv
import numpy as np

img = cv.imread(r"Project1\Image\building.webp")

# resize: make an image bigger or smaller
# resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
# cv.imshow("Resized Image", resized)

# flippping: reversing an image either:
# 1. ↔️ Left to right (horizontal flip) -> 1
# 2. ↕️ Top to bottom (vertical flip) -> 0
# 3. 🔁 Both directions -> -1
# flipped = cv.flip(img, 1)
# cv.imshow("Original Image", img)
# cv.imshow("Flipped Image", flipped)

# cropping: selecting and cutting out a specific part of an image.
# cropped = img[100:500, 200:300]
# cv.imshow("Original Image", img)
# cv.imshow("Cropped Image", cropped)

# translation: shifting an image from one position to another in the X (left-right) and Y (up-down) direction.
# def translate(img, x, y): 
#     trans_mat = np.float32([[1, 0, x], [0, 1, y]])
#     dimension = (img.shape[1], img.shape[0])  #(width , height)
#     return cv.warpAffine(img, trans_mat, dimension)

# translated = translate(img, 200, 100)
# cv.imshow("Original Image", img)
# cv.imshow("Translated Image", translated)

# rotation: spinning an image clockwise or anti-clockwise
def rotate(img, angle, rotpoint = None):
    (height, width) = img.shape[:2]  # 0 -> height & 1 -> width
    if rotpoint is None:
        rotpoint = (width // 2, height // 2)
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate(img, 45)
cv.imshow("Original Image", img)
cv.imshow("Rotated Image", rotated)

cv.waitKey(0)