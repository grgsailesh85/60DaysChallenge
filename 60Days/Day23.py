import cv2 as cv  # Import OpenCV library
# Load Haar Cascade model for face detection
face_casade = cv.CascadeClassifier(
        cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )

# Open webcam (0 = default camera)
cap = cv.VideoCapture(0)

while True:
    # Read frame from webcam
    tr, frame = cap.read()

    # Convert frame to grayscale (needed for Haar Cascade)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_casade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5
        )
    # Draw rectangle around each detected face
    for (x, y, w, h) in faces:
        cv.rectangle(
                frame,
                (x, y),              # top-left corner
                (x + w, y + h),      # bottom-right corner
                (0, 255, 0),         # green color
                2                    # thickness
            )
    # Show the output frame
    cv.imshow("Face Detection", frame)

    # Exit loop when 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam resource
cap.release()

# Close all OpenCV windows
cv.destroyAllWindows()