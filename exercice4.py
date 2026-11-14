
import dlib
import cv2

detector = dlib.get_frontal_face_detector()

img = cv2.imread("images/people.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = detector(gray)

for face in faces:
    x = face.left()
    y = face.top()
    w = face.width()
    h = face.height()

    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("Visages détectés", img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 