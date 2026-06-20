import cv2 as cv                     # Import the OpenCV library and give it the alias 'cv'

# Read the image from the Image folder
img = cv.imread(r"Image\bruno.jpg")

# Convert the color image (BGR) to a grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Load the pre-trained Haar Cascade face detection model
face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces in the grayscale image
faces = face_cascade.detectMultiScale(
    gray,                 # Input grayscale image
    scaleFactor=1.1,      # Reduce image size by 10% at each scan
    minNeighbors=5        # A face must have at least 5 neighboring detections
)

# Loop through every detected face
# Each face returns (x, y, width, height)
for (x, y, w, h) in faces:

    # Draw a green rectangle around the detected face
    cv.rectangle(
        img,                    # Original image to draw on
        (x, y),                 # Top-left corner of rectangle
        (x + w, y + h),         # Bottom-right corner of rectangle
        (0, 255, 0),            # Rectangle color (Green in BGR format)
        2                       # Rectangle thickness (2 pixels)
    )

# Display the image in a window named "FACES"
cv.imshow("FACES", img)

# Wait indefinitely until a key is pressed
cv.waitKey(0)
