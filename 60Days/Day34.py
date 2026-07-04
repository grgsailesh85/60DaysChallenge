import cv2 as cv
import numpy as np

# load the image
image_path = r"training_images\Elon_Musk\EM11.jpg"
image = cv.imread(image_path)

# convert into HSV format
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# define the skin color range in hsv
lower_skin = np.array([0, 20, 70], dtype = np.uint8)
upper_skin = np.array([20, 255, 255], dtype = np.uint8)

# define the mask
img_mask = cv.inRange(hsv_image, lower_skin, upper_skin)

# apply the mask to the original image
detected_skin = cv.bitwise_and(image, image, mask = img_mask)

# display the images
detected = cv.resize(detected_skin, (500, 400))
org = cv.resize(image, (500, 400))
mask_r = cv.resize(img_mask, (500, 400))
cv.imshow("Original Image", org)
cv.imshow("Mask", mask_r)
cv.imshow("Skin Detected", detected)

cv.waitKey(0)
cv.destroyAllWindows()