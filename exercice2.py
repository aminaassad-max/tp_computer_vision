import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

cap=cv2.VideoCapture(1)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc=cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter('sortie_gris.mp4',fourcc,20.0,(w,h),isColor=False)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(gray)
    cv2.imshow('Enregistrement',gray)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
#question
#Que se passe-t-il si vous utilisez une vidéo enregistrée à la place de la webcam ? 
#Le traitement reste le même :
#- chaque frame de la vidéo est récupérée avec cap.read();
#- elle peut être convertie en niveaux de gris ;
#- elle peut être affichée ou enregistrée dans une nouvelle vidéo.