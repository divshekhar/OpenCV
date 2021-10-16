import cv2 as cv
import numpy as np

eye_cascade = cv.CascadeClassifier('./haarcascade_eye_tree_eyeglasses.xml')

face_cascade = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
# Read the input image
# img = cv.imread('../img/rohit.jpg')
cap = cv.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 3)
    #To display a image
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
