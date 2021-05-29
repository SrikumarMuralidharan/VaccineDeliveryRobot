#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:12:47 2021

@author: srikumar
"""

import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(31,gpio.OUT)         #IN1
    gpio.setup(33,gpio.OUT)         #IN2
    gpio.setup(35,gpio.OUT)         #IN3
    gpio.setup(37,gpio.OUT)         #IN4
    
def gameover():
    #set all pins low
    gpio.output(31, False)
    gpio.output(33, False)
    gpio.output(35, False)
    gpio.output(37, False)
    
def forward(tf):
    init()
    # Left wheels
    gpio.output(31, True)
    gpio.output(33, False)
    # Right wheels
    gpio.output(35, False)
    gpio.output(37, True)
    # Wait
    time.sleep(tf)
    # Send all pins low and cleanup
    gameover()
    gpio.cleanup()
    
def reverse(tf):
    init()
    # Left wheels
    gpio.output(31, False)
    gpio.output(33, True)
    # Right wheels
    gpio.output(35, True)
    gpio.output(37, False)
    # Wait
    time.sleep(tf)
    # Send all pins low and cleanup
    gameover()
    gpio.cleanup()
    
def pivotleft(tf):
    init()
    # Left wheels
    gpio.output(31, False)
    gpio.output(33, True)
    # Right wheels
    gpio.output(35, False)
    gpio.output(37, True)
    # Wait
    time.sleep(tf)
    # Send all pins low and cleanup
    gameover()
    gpio.cleanup()
    
def pivotright(tf):
    init()
    # Left wheels
    gpio.output(31, True)
    gpio.output(33, False)
    # Right wheels
    gpio.output(35, True)
    gpio.output(37, False)
    # Wait
    time.sleep(tf)
    # Send all pins low and cleanup
    gameover()
    gpio.cleanup()

    
forward(2)
time.sleep(1)    
reverse(2)
time.sleep(1)    
pivotleft(2)
time.sleep(1)    
pivotright(2)