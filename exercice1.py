import cv2

img = cv2.imread('images/image1.jpeg')

cv2.imshow('Image originale', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image en niveaux de gris', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

edges=cv2.Canny(img,100,200)
cv2.imshow('Contours detectes',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#questions
#1.La matrice retournee par OpenCV represente l’image sous forme d’un tableau de pixels, ou chaque element contient les valeurs d’intensite ou de couleur (BGR) associees a chaque pixel de l’image.
#2. Pourquoi convertit-on souvent l’image en niveaux de gris avant traitement ?
#On convertit l'image en niveaux de gris pour plusieurs raisons :
#- Reduire la complexite : une image couleur possede 3 canaux (B, G, R), alors qu'une image en gris possede un seul canal.
#- Reduire le temps de calcul : les algorithmes de traitement d'image travaillent plus rapidement avec une seule matrice.
#- Faciliter l'extraction des caracteristiques : beaucoup de traitements comme la detection de contours, la detection de formes ou la segmentation utilisent uniquement l'intensite lumineuse.
#- Supprimer l'information de couleur qui n'est pas toujours necessaire.#

#3. Que peut nous apporter le filtre Gaussien ?
#Le filtre Gaussien est un filtre de lissage (smoothing) qui permet de reduire le bruit dans une image.



