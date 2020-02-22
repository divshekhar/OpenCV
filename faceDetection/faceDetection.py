import cv2 as cv
import numpy as np

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

    # Display the Image
    cv.imshow('Image', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
