# Edges -> In image processing, an edge is the boundary where the brightness or color changes suddenly.
# Contour -> A contour is the continuous outline or boundary of an object in an image, formed by connecting points with the same intensity or along the object's edge.

import cv2 as cv

img = cv.imread(r"Project1\Image\building.webp")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred_img = cv.GaussianBlur(gray, (5, 5), 0)

# Canny 
edges = cv.Canny(blurred_img, 100, 200)
contours_canny, _ =  cv.findContours(edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count1 = len(contours_canny)
print(count1)


# Threshold
thres_val, thres_img = cv.threshold(blurred_img, 180, 255, cv.THRESH_BINARY)
contours_thres, _ = cv.findContours(thres_img, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
count2 = len(contours_thres)
print(count2)

# Draw the Contours
img_thres = gray.copy()
img_canny = gray.copy()

cv.drawContours(img_canny, contours_canny, -1, (0, 255, 0), 2)
cv.drawContours(img_thres, contours_thres, -1, (0, 0, 255), 2)

cv.imshow("Contour_Canny", img_canny)
cv.imshow("Contour_Thres", img_thres)


cv.waitKey(0)
cv.destroyAllWindows()
