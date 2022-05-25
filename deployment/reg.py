import cv2
from flask import request

def regii(id):
    key = 0
    while(key<1):
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        IMAGE_PATH ='deployment\stud_images\Images' 
        cv2.imshow(IMAGE_PATH + "/{}".format(id) , image)
        cv2.imwrite(IMAGE_PATH + "/{}".format(id) + ".jpg", image)

        cv2.waitKey(1)
        key += 1

def regi():
    id = request.form['name']
    regii(id)
