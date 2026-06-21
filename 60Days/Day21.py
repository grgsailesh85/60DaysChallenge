# blurring -> image processing technique used to smooth an image by reducing details, sharp edges, and noise.
# Blurring makes neighboring pixels look more similar by averaging their values.
import cv2 as cv

img = cv.imread(r"Project1\Image\cr7.jpg")
resized = cv.resize(img, (600, 500))
cv.imshow("Image", resized)

# average blurring -> Takes the average of neighboring pixels.
# avg_blur = cv.blur(resized, (5, 5))
# cv.imshow("Average Blur", avg_blur)

# median bluring -> Replaces each pixel with the median value.
# median_blur = cv.medianBlur(resized, 5)
# cv.imshow("Median Blur", median_blur)

# gaussian blur -> Applies more weight to nearby pixels and less weight to distant ones.
# Gauss_Blur = cv.GaussianBlur(resized, (5, 5), 0)
# cv.imshow("G_Blur", Gauss_Blur)

# bilateral blur -> Smooths the image while preserving edges.
bilateral = cv.bilateralFilter(resized, 5, 15, 15)
cv.imshow("Bilateral_Blur", bilateral)
cv.waitKey(0)
