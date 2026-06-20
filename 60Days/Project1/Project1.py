import cv2 as cv
#Reading Images
img = cv.imread(r"Image\cr7.jpg")
# cv.imshow("Image", img)

resized = cv.resize(img, (500, 500))
# cv.imshow("Image", resized)

# flipped = cv.flip(resized, 0)
# cv.imshow("Image", flipped)

# gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray-Image", gray)

# cv.rectangle(img, (200, 200), (400, 400), (0, 0, 255), 2)
# cv.imshow("Image", img)

#edge detection 
#canny -> ml model -> pre-trained
edges = cv.Canny(img, threshold1=100, threshold2=200) 
cv.imshow("Edges", edges)

cv.waitKey(0)