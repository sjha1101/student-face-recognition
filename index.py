# OpenCV import karna
import cv2

# Load Haar Cascade Classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# Haar Cascade ek pre-trained model hai jo images me faces detect karta hai.
# cv2.data.haarcascades → OpenCV ke andar stored Haar cascade files ka path.
# "haarcascade_frontalface_default.xml" → file jo specifically frontal (samne se) faces detect karti hai.

# 3)Camera open karna
# Ye webcam ko start karta hai.
# 0 → default webcam. Agar multiple cameras hote, to 1, 2 likh ke alag camera 
# select kar sakte ho.
cap = cv2.VideoCapture(0)

while True:
#     4. Video frame by frame read karna
#     Har loop me ek frame (image) webcam se capture hoti hai.
# ret → True/False return karta hai (frame mila ya nahi).
# frame → actual image data (color image).
    ret, frame = cap.read()
    if not ret:
        break

#    5. Gray scale me convert karna
# Haar Cascade sirf grayscale images pe kaam karta hai, isliye frame ko black & white banaya gaya.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     6. Face detection
#     Yaha Haar Cascade detect karega ki image me face kaha kaha hai.
# scaleFactor=1.3 → image ko har step me thoda shrink karke detect karta hai (1.1 = slow, 1.3 = fast but less accurate).
# minNeighbors=5 → jitni baar ek face confirm hoga utna hi valid mana jayega (chhoti value = more detections, zyada false detections).
# faces ek list deta hai: [ (x, y, w, h), (x, y, w, h), ... ]
# Matlab agar 2 faces hai, to 2 sets of coordinates milenge.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

#    7. Rectangle draw karna
# Har face ke liye rectangle banega:
# (x, y) → rectangle ka top-left corner.
# (x+w, y+h) → bottom-right corner.
# (0, 255, 0) → Green color (BGR format).
# 2 → line thickness.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#    8. Output dikhana
# 👉 Ye ek window kholta hai jisme live video feed dikhega, aur faces ke around green rectangle banenge.
    cv2.imshow("Face Detection", frame)

# 9. Loop se exit condition
# Agar user q press kare, to loop break ho jata hai aur webcam stop ho jata hai.
    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 10. Resources release karna
# cap.release() → webcam ko free kar deta hai.
# cv2.destroyAllWindows() → saari OpenCV windows close ho jaati hain.
# Release resources
cap.release()
cv2.destroyAllWindows()
