import cv2
import numpy as np 
import face_recognition

ielon = face_recognition.load_image_file('Images\elontry.jpg')
ielon = cv2.cvtColor(ielon,cv2.COLOR_BGR2RGB)

ielontry = face_recognition.load_image_file('Images\obama.png')
ielontry = cv2.cvtColor(ielontry,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(ielon)[0]
encodeelon = face_recognition.face_encodings(ielon)[0]
cv2.rectangle(ielon,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

faceloctry = face_recognition.face_locations(ielontry)[0]
encodeelontry = face_recognition.face_encodings(ielontry)[0]
cv2.rectangle(ielontry,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeelon],encodeelontry)
facedis = face_recognition.face_distance([encodeelon],encodeelontry)
print(results,facedis)
cv2.putText(ielon,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('elon',ielontry)
cv2.imshow('elontry',ielon)
cv2.waitKey(0)