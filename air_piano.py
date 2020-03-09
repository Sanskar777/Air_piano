import numpy as np
from time import sleep
import cv2
import time
from playsound import playsound

cap = cv2.VideoCapture(0)
# cap.set(3,720)
# cap.set(4,720)
while(True):
    # try:
    ret, s = cap.read()
    s=cv2.flip(s,1)
    s = cv2.cvtColor(s,cv2.COLOR_BGR2GRAY)
    # if count==prev_count and count==0:
    #     first_img = s

    cv2.imshow('frame', s)
    blurred_img = cv2.blur(s, (3, 3))
    # cv2.imshow('blurred image', blurred_img)
    edges = cv2.Canny(blurred_img,50,160)
    # edges = cv2.createBackgroundSubtractorMOG2().apply(edges)
    ret,thresholded_img = cv2.threshold(edges,100,255,cv2.THRESH_BINARY)
    contours,heirarchy = cv2.findContours(thresholded_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours]
    index = np.argmax(areas)
    largest_contour = contours[index]
    # drawing = np.zeros((thresholded_img.shape[0],thresholded_img.shape[1],1),np.uint8)
    #dimensions=thresholded_img.shape
    #print(dimensions)
    cv2.drawContours(thresholded_img,contours,index,255,3)
    #x=640
    #y=
    start_point=(0,75+75)
    end_point=(30,0+75)
    color = (255, 0, 0) 
    thickness = 2
    
    for i in range(0,640,30):
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
      start_point=(i,75+75)
      end_point=(30+i,0+75)
    for i in range(0,3):
      start_point=(20+i*210,225+75)
      end_point=(i*210+40,75+75)
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
      start_point=(i*210+50,225+75)
      end_point=(i*210+70,75+75)
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
      start_point=(i*210+110,225+75)
      end_point=(i*210+130,75+75)
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
      start_point=(i*210+140,225+75)
      end_point=(i*210+160,75+75)
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
      start_point=(i*210+170,225+75)
      end_point=(i*210+190,75+75)
      thresholded_img = cv2.rectangle(thresholded_img, start_point, end_point, color, thickness)
   #let the input detected be an array of bool values corresponding to each key k[36]
   for i in range(0,36):
     if(k[i]):
        playsound(str(i)+'.mp3')          
      
    cv2.imshow('drawing the hand', thresholded_img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    # except:
    # if cv2.waitKey(20) & 0xFF == ord('q'):
    # break
cap.release()
cv2.destroyAllWindows()
