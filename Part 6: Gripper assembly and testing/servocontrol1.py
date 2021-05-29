#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:58:18 2021

@author: srikumar
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import imutils
import datetime
import RPi.GPIO as GPIO


def Main():    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(36, GPIO.OUT)
    pwm = GPIO.PWM(36,50)
    pwm.start(7.5)
#initialize the Raspberry Pi camera
    camera=PiCamera()
    camera.resolution=(640,480)
    camera.framerate=10
    rawCapture=PiRGBArray(camera,size=(640,480))
    time.sleep(0.5)
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('Gripper.avi',fourcc,10,(640,480))
    #allow the camera to warmup
    time.sleep(0.1)
    
    i= 7.5
    counter = 0
    
    for frame in camera.capture_continuous(rawCapture,format="bgr",use_video_port=False):
        image = frame.array
        img1 = cv2.flip(image,-1)
        if counter==0:
            i+=0.5
            print(i)
            if (i==12.5):
                counter=1
        if counter==1:
            if i==7.0:
                break
            i-=0.5
            print(i)
        pwm.ChangeDutyCycle(i)
        cv2.putText(img1,'Duty:'+str(i)+'%',(10,100),cv2.FONT_HERSHEY_DUPLEX,3,(255,0,255),2)
        time.sleep(0.5)
        #show the frame to our screen
        cv2.imshow("Final",img1)
        out.write(img1)
        rawCapture.truncate(0)
    
    out.release()
    cv2.destroyAllWindows()
    pwm.stop()
    GPIO.cleanup()
        
if __name__ == '__main__':
    Main()