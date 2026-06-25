import cv2 as cv
import matplotlib.pyplot as plt
# Threshold -> Threshold is a cutoff value that separates pixels into different groups, usually black and white.

img = cv.imread(r"Project1\Image\building.webp")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Image", gray)

# # ---------------- SIMPLE THRESHOLD ----------------
# # Apply Binary Threshold
# # Pixel > 135  -> 255 (White)
# # Pixel <= 135 -> 0 (Black)
# threshold, thres_img = cv.threshold(
#     gray,
#     135,                 # Threshold value
#     255,                 # Maximum value assigned
#     cv.THRESH_BINARY     # Binary threshold type
# )
# # Apply Inverse Binary Threshold
# # Pixel > 135  -> 0 (Black)
# # Pixel <= 135 -> 255 (White)
# threshold, thres_img_inv = cv.threshold(
#     gray,
#     135,                     # Threshold value
#     255,                     # Maximum value assigned
#     cv.THRESH_BINARY_INV     # Inverse binary threshold
# )
# # Display binary threshold image
# cv.imshow("Simple Threshold image Regular", thres_img)
# # Display inverse binary threshold image
# cv.imshow("Simple Threshold image Inverse", thres_img_inv)



# # Adaptive Thresholding is a thresholding technique where the threshold value is calculated separately for different parts of the image.
# # Apply adaptive threshold
# adaptive_thres_img_mean = cv.adaptiveThreshold(
#         gray,                           # Grayscale image
#         255,                            # Maximum value
#         cv.ADAPTIVE_THRESH_MEAN_C,      # Adaptive method
#         cv.THRESH_BINARY,               # Binary threshold
#         11,                             # Neighborhood size
#         2                               # Constant subtracted
#     )
# adaptive_thres_img_gauss = cv.adaptiveThreshold(
#         gray,                           # Grayscale image
#         255,                            # Maximum value
#         cv.ADAPTIVE_THRESH_GAUSSIAN_C,  # Adaptive method
#         cv.THRESH_BINARY,               # Binary threshold
#         11,                             # Neighborhood size
#         2                               # Constant subtracted
#     )
# cv.imshow("Adaptive Threshold (Mean)", adaptive_thres_img_mean)
# cv.imshow("Adaptive Threshold (Gaussian)", adaptive_thres_img_gauss)



# color spaces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # -> Gray
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# cv.imshow("Gray_IMG", gray)
# cv.imshow("HSV_IMG", hsv)
# cv.imshow("HLS_IMG", hls)
# cv.imshow("YCRCB_IMG", ycrcb)
# cv.imshow("RGB_IMG", rgb)

plt.imshow(rgb)
plt.show()


# Wait until a key is pressed
cv.waitKey(0)