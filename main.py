import cv2

#Load the Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Read the input image
img = cv2.imread('lionel.jpg')

#Convert into Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)

#Detect Faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
font = cv2.FONT_HERSHEY_SIMPLEX

#Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#Display the output
cv2.imshow('img', img)
cv2.waitKey()




