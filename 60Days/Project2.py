import cv2 as cv
import numpy as np
import os # -> to navigate inside/ through folders

# Haar cascade Load
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

# Load the recognizer
recognizer = cv.face.LBPHFaceRecognizer_create()

dataset_path = "training_images"

faces = []
labels = []

labels_to_name = {}
current_label = 0

for person_name in os.listdir(dataset_path):
    person_folder = os.path.join(dataset_path, person_name)
    
    labels_to_name[current_label] = person_name
    
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        
        image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
        
        face_rect = face_cascade.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 5)
        
        for (x, y, w, h) in face_rect: 
            # Crop and resize the faces
            face_roi = image[y:y+h, x:x+w]
            
            face_resized = cv.resize(face_roi, (100, 100))
            
            faces.append(face_resized)
            labels.append(current_label)
            
    current_label += 1    # current_label = current_label + 1

faces = np.array(faces)
labels = np.array(labels)

recognizer.train(faces, labels)
print("Training Complete!")

test_img = cv.imread(r"Elon_musk.jpg")
test_gray = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)

face_rectangle = face_cascade.detectMultiScale(test_gray, scaleFactor = 1.2, minNeighbors = 8)

for (x, y, w, h) in face_rectangle:
    face_roi = test_gray[y:y+h, x:x+w]
    face_resized = cv.resize(face_roi, (100, 100))
    
    label, confidence = recognizer.predict(face_resized)
    
    person_name = labels_to_name[label]
    
    text = f"{person_name} ({round(confidence, 2)})"  # -> Elon_Musk 80.88
    
    cv.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    cv.putText(test_img, text, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


test_img = cv.resize(test_img, (600, 600))
cv.imshow("Result", test_img)
cv.waitKey(0)
cv.destroyAllWindows()
