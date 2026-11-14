import cv2
import face_recognition

# Charger l'image
img = cv2.imread("images/people.jpg")

# Vérifier que l'image est bien chargée
if img is None:
    print("Image introuvable")
    exit()

# Conversion BGR vers RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Détecter les landmarks du visage
landmarks_list = face_recognition.face_landmarks(rgb)

print("Nombre de visages détectés :", len(landmarks_list))

# Dessiner les 68 points
for landmarks in landmarks_list:
    for partie, points in landmarks.items():
        # parties possibles :
        # chin, left_eye, right_eye, nose_tip, top_lip, bottom_lip...

        for (x, y) in points:
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)


# Afficher l'image
cv2.imshow("Facial landmarks", img)

cv2.waitKey(0)
cv2.destroyAllWindows()