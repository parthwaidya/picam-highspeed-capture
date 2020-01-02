#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:44:28 2020

@author: Parth
"""
# A code for capturing high speed photos from raspberry pi and uploading it to a php based server
import picamera
import time
import datetime
import os
import requests

NUMPHOTOS = 5 #click 5 photos in burst

def capture():
    with picamera.PiCamera() as camera:
        time.sleep(2)
        camera.resolution = (3280, 2464)
        camera.shutter_speed = 12000
        time.sleep(15)
        
        #additional settings
        
        #camera.color_effects=(128,128)
        #camera.exposure_mode='sports'
        #camera.framerate=60
        #time.sleep(4) #give the exposure mode time to adjust
        #camera.iso = 1600
        
        currentDT = datetime.datetime.now()
        date = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
        camera.capture_sequence(('photos/'+date+'_%03d.png' % i for i in range(0,NUMPHOTOS)), use_video_port=False)

    
def upload():
    for root, dirs, files in os.walk("frames"):
        for filename in files:
            try:
                print("Trying to upload : " +filename)
                url = 'http://localhost/upload_photo.php'
                files = {'file': open('photos/'+filename, 'rb')}
                r = requests.post(url, files=files)
                print("Response code : " + r)
                #optionally, remove the file after upload is complete
            	#os.remove('photos/'+filename) 
            except:
                print("Exception")

capture()
upload()


