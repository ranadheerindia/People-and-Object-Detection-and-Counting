# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 19:05:29 2019

@author: 30030385
"""
path = 'C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Images\\'
#images = [cv2.imread(file) for file in glob.glob(path+"**\*.jpg")]
import glob
import os
import cv2
cap = cv2.VideoCapture("C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\video\\cut.mp4")

#full_names = [f for f in glob.glob(path+"*.jpg")]
#files = [os.path.basename(x) for x in glob.glob(path+"*.jpg")]

from imageai.Detection import ObjectDetection
detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath('C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\yolo-tiny.h5')
detector.loadModel()

j = 0
count = 0
while cv2.waitKey(1) < 0:
    hasFrame,frame = cap.read()
    if count%15 == 0 : #Each frame
          # Stop the program if reached end of video
        if not hasFrame:
            print("Done processing !!!")
#            print("Output file is stored as ", outputFile)
            cv2.waitKey(3000)
            break
    cv2.imwrite('C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\temp\\input\\' + str(j)+".jpg",frame)    
#   detection = detector.detectObjectsFromImage(input_image= 'C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\temp\\input\\' + str(j)+".jpg" , output_image_path='C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\output\\' + str(j)+".jpg")   
        
    
    detection = detector.detectObjectsFromImage(input_image= 'C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\temp\\input\\' + str(j)+".jpg"  , output_image_path='C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\temp\\output\\' + str(j)+".jpg")       
    img = cv2.imread('C:\\Users\\30030385\\Desktop\\Adani\\Projects\\ACH Canteen\\Python\\TinyYolo\\temp\\output\\' + str(j)+".jpg")
    cv2.imshow('winName', img)
    j +=1
for eachItem in detection:
    print(eachItem["name"] , " : ", eachItem["percentage_probability"])
    
cv2.destroyAllWindows()

