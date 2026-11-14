import face_recognition
import os

# Désactiver CUDA pour dlib (utiliser le CPU)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Charger l'image de référence
image_ref = face_recognition.load_image_file("images/ref.jpg")

# Extraire l'encodage du visage de référence
encodage_ref = face_recognition.face_encodings(image_ref)[0]


# Charger l'image test
image_test = face_recognition.load_image_file("images/test.jpg")

# Extraire l'encodage du visage test
encodage_test = face_recognition.face_encodings(image_test)[0]


# Comparer les deux visages
resultat = face_recognition.compare_faces(
    [encodage_ref],
    encodage_test
)


# Afficher le résultat
if resultat[0]:
    print("Même personne ? True")
else:
    print("Même personne ? False")