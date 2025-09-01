import cv2
import os
import face_recognition
import pickle

dataset_path = "dataset"
encodings = []
names = []

# Loop through all folders in dataset
for student_folder in os.listdir(dataset_path):
    student_path = os.path.join(dataset_path, student_folder)
    if not os.path.isdir(student_path):
        continue

    roll_no, name = student_folder.split("_", 1)

    # Loop through all images inside student's folder
    for img_name in os.listdir(student_path):
        img_path = os.path.join(student_path, img_name)
        image = cv2.imread(img_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect face encodings
        boxes = face_recognition.face_locations(rgb, model="hog")
        encs = face_recognition.face_encodings(rgb, boxes)

        for enc in encs:
            encodings.append(enc)
            names.append(f"{roll_no}_{name}")

print(f"[INFO] Encoded {len(encodings)} faces.")

# Save encodings to file
data = {"encodings": encodings, "names": names}
with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encodings saved to encodings.pkl")
