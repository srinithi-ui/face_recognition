import cv2
import numpy as np 
import face_recognition
import os
from datetime import datetime

path = 'deployment/stud_images/Images'
images = []
cnames = []
mylst = os.listdir(path)

for cl in mylst:
    currimg = cv2.imread(f'{path}/{cl}')
    images.append(currimg)
    cnames.append(os.path.splitext(cl)[0])


def find_encodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markattendance(name):
    with open('attendance_in.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
#markattendance('srinithi')

encodelistknown = find_encodings(images)




def att():
    key = 0
    while (key<1):
        cap = cv2.VideoCapture(0)
        success,img = cap.read()
        imgs = cv2.resize(img,(0,0),None,0.25,0.25)
        imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
        facescurrent = face_recognition.face_locations(imgs)
        encodecurrent = face_recognition.face_encodings(imgs,facescurrent)

        for encodeface,faceloc in zip(encodecurrent,facescurrent):
            match = face_recognition.compare_faces(encodelistknown,encodeface)
            facedis = face_recognition.face_distance(encodelistknown,encodeface)
       # print(facedis)
            matchindex = np.argmin(facedis)

            if match[matchindex]:
                name = cnames[matchindex].upper()
            #print(name)
                y1,x2,y2,x1 = faceloc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markattendance(name)
        cv2.imshow('Webcam',img)
        cv2.waitKey(1)
        key +=1
       

att()