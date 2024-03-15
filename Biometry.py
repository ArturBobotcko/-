import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
image = cv2.imread('photos/test_photo.jpg')
image_original = image.copy()
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(image, 1.4, 4)
eyes = eye_cascade.detectMultiScale(image, 1.4, 4)
for(x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
  roi_gray = gray_image[y:y+h, x:x+w]
  roi_color = image[y:y+h, x:x+w]
  eyes = eye_cascade.detectMultiScale(roi_gray)
  for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
combined_image = cv2.hconcat([image_original, image])
cv2.imshow('Original vs Processed', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()