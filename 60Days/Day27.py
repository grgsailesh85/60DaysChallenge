import cv2 as cv
import numpy as np

# Masking
img = cv.imread(r"Project1\Image\RM.webp")

resized_img = cv.resize(img, (900, 1200))

# # Masking -> Masking means creating a True/False filter to work only with the elements that satisfy a condition.
# # Create a mask
# img_mask = np.zeros(resized_img.shape[:2], dtype = "uint8")
# # Create a white circle in the mask
# cv.circle(img_mask, (350, 400), 350, 255, -1)
# # Apply the mask
# masked_img = cv.bitwise_and(resized_img, resized_img, mask = img_mask) 
# # Show
# cv.imshow("Original", resized_img)
# cv.imshow("Mask", img_mask)
# cv.imshow("Masked image", masked_img)


# Splitting the Channels
B, G, R = cv.split(resized_img)
# cv.imshow("Original Image", resized_img)
# cv.imshow("Gray -> Blue", B)
# cv.imshow("Gray -> Green", G)
# cv.imshow("Gray -> Red", R)
# merged = cv.merge([B, G, R])
# cv.imshow("Merged_Image", merged)

zeros = np.zeros_like(B)
Blue_visual = cv.merge([B, zeros, zeros])
Green_visual = cv.merge([zeros, G, zeros])
Red_visual = cv.merge([zeros, zeros, R])
cv.imshow("Blue", Blue_visual)
cv.imshow("Green", Green_visual)
cv.imshow("Red", Red_visual)





cv.waitKey(0)
cv.destroyAllWindows()