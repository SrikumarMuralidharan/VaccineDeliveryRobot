#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 10:30:06 2021

@author: srikumar
"""

## Run on RaspberryPi after installing required packages.

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import imutils
import datetime

#initialize the Raspberry Pi camera
camera=PiCamera()
camera.resolution=(640,480)
camera.framerate=30
rawCapture=PiRGBArray(camera,size=(640,480))
time.sleep(0.5)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Sriku_video.avi',fourcc,10,(640,480))
#allow the camera to warmup
time.sleep(0.1)


file = open('hw3data.txt','a')
i=0

for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=False):
    
    start = datetime.datetime.now()
    #grab the currennt frame
    image=frame.array
    
    image = cv2.flip(image,-1)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    minHSV = np.array([60,45,200])
    maxHSV = np.array([80,145,255])
    maskHSV = cv2.inRange(hsv_image,minHSV,maxHSV)
    canvas = np.full(image.shape, fill_value=255,dtype="uint8")
    resultHSV = cv2.bitwise_and(canvas, canvas, mask=maskHSV)
    contours = cv2.findContours(maskHSV.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    conts = imutils.grab_contours(contours)
    if len(conts) > 0:   
        c = max(conts,key=cv2.contourArea)
        ((Cx,Cy),r) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]) , int(M["m01"]/M["m00"]))
        final = cv2.circle(image.copy(),(int(Cx),int(Cy)),int(r),(0,255,255),2)
        cv2.circle(final,center,3,(0,0,255),-1)
    
  	#show the frame to our screen
    cv2.imshow("Frame",final)
    out.write(final)
    stop = datetime.datetime.now()
    now = (stop-start)
    outstring = str(now.total_seconds())+ '\n'
    print(now.total_seconds())
    file.write(outstring)
    i += 1
    print("i",i)
    
    
    key=cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    if key==ord("q"):
        break
cv2.destroyAllWindows()