#-*- encoding:utf-8 -*-
import sys
from pytube import YouTube
import cv2
import os

def vidGetter(save_path): #video downloader
    tubeURL = input("Enter url to get video : ")
    second = (int)(input("How long interval do you want(second)? : "))
    yt = YouTube(tubeURL)    
 
    print(yt.title)
    yt.streams.first().download(save_path)
    return yt.title, second

def toFrames(vid_path, vid_name, seconds):
    cap = cv2.VideoCapture(vid_name)

    try:
        if not os.path.exists('frame'):
            os.makedirs('frame')
    except OSError:
        print ('Error: Creating directory of frame')

    vidcap = cv2.VideoCapture(vid_name)
    currentFrame = 0
    while(True):
        success,image = vidcap.read()
        if not success:
            break
        ret, frame = cap.read()

        if(currentFrame % (seconds*30) == 0):
            name = './frame/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)

        currentFrame += 1
    cap.release()

vidname, split_second = vidGetter(os.getcwd())
toFrames(os.getcwd() + "\\" + vidname + ".mp4", vidname + ".mp4", split_second)
os.remove(os.getcwd() + "\\" + vidname + ".mp4")