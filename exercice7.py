from ultralytics import YOLO
import cv2
import os

# Charger le modèle YOLOv8 léger
model = YOLO("yolov8n.pt")

# Image de test
image_path = "images/image_objects.jpg"

# Vérifier si l'image existe
if not os.path.exists(image_path):
    print("Image non trouvée, utilisation de people.jpg")
    image_path = "images/people.jpg"


try:
    # Détection des objets
    results = model(image_path, conf=0.5)

    # Récupérer l'image avec les détections
    img_result = results[0].plot()

    # Afficher le résultat
    cv2.imshow("Detection YOLO", img_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print("Erreur lors de la détection :", e)