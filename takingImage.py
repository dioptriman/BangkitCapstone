#!/Users/andhikaagungpratama/myenv/bin/python
import cv2 
import numpy as np 
import time
import datetime
cap = cv2.VideoCapture(0) 
nframes = 1024
interval = 5


for i in range(nframes):
    # capture
    ret, img = cap.read()
    # save file
    cv2.imwrite('./Image/img_'+str(i).zfill(4)+"_"+str(datetime.datetime.now())+'.png', img)
    # wait 5 seconds
    time.sleep(interval)