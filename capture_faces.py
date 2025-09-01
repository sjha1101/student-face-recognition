import cv2
import os

# Student info
roll_no = input("Enter Roll No: ")
name = input("Enter Name: ")

dataset_path = f"dataset/{roll_no}_{name}"
os.makedirs(dataset_path, exist_ok=True)

# Haar Cascade load
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(f"{dataset_path}/face_{count}.jpg", face_img)
        count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Capture - Press q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") or count >= 50:
        break

cap.release()
cv2.destroyAllWindows()
