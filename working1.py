import numpy as np
from time import sleep
import cv2
import time
from skimage.measure import compare_ssim
import argparse
import imutils

cap = cv2.VideoCapture(0)

count=0
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame = cv2.flip(frame,0)
    im = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if count==1:
        grayA = prev_im
        grayB = im
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        #print("SSIM: {}".format(score))
        thresh = cv2.threshold(diff, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cv2.imshow("Original", grayA)
        cv2.imshow("Modified", grayB)

        cv2.imshow("Thresh", thresh)

        c = max(cnts, key=cv2.contourArea)
        #extLeft = tuple(c[c[:, :, 0].argmin()][0])
        #extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        #cv2.circle(frame, extLeft, 8, (0, 0, 255), -1)
        #cv2.circle(frame, extRight, 8, (0, 255, 0), -1)
        cv2.circle(frame, extTop, 8, (0, 255, 0), -1)

        prev_im = im
        num_keys = 21
        width, height = frame.shape[1],frame.shape[0]
        y0 = height//2
        x_width = width//num_keys
        start_point=(0,y0)
        end_point=(x_width,0)
        color = (0, 0, 0)
        thickness = 2

        for i in range(0,num_keys):
          start_point=(i*x_width,150)
          end_point=(x_width+start_point[0],height)
          frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        cv2.imshow("Diff1", frame)
        for i in range(0,3):
          start_point=(20+i*210,y0+100)
          end_point=(i*210+40,150)
          frame = cv2.rectangle(frame, start_point, end_point, color, -1)
          start_point=(i*210+50,y0+100)
          end_point=(i*210+70,150)
          frame = cv2.rectangle(frame, start_point, end_point, color, -1)
          start_point=(i*210+110,y0+100)
          end_point=(i*210+130,150)
          frame = cv2.rectangle(frame, start_point, end_point, color, -1)
          start_point=(i*210+140,y0+100)
          end_point=(i*210+160,150)
          frame = cv2.rectangle(frame, start_point, end_point, color, -1)
          start_point=(i*210+170,y0+100)
          end_point=(i*210+190,150)
          frame = cv2.rectangle(frame, start_point, end_point, color, -1)

        # boundaries = [([0,200,0],[0,255,0])]
        # for (lower,upper) in boundaries:
        #     lower = np.array(lower,dtype = 'uint8')
        #     upper = np.array(upper,dtype = 'uint8')
        #     mask = cv2.inRange(frame,lower,upper)
        #     output = cv2.bitwise_and(frame,frame,mask=mask)
        #     for i in range(frame.shape[0]):
        #         for j in range(frame.shape[1]):
        #             if(frame[i][j][1]>200):
        #                 detected_point=(i,j)
        #                 break
        #         break
        # cv2.circle(frame,(detected_point[0],detected_point[1]),8,(255,0,0),-1)
        cv2.imshow("Diff", frame)

        #code for k array
        #int num=len(extTop)
        pkeys=np.zeros(36)
        x_key = extTop[0]
        y_key = extTop[1]
        if y_key < (y0+100):
          if x_key < 20:
            pkeys[0]=1
          elif x_key < 40:
            pkeys[21]=1
          elif x_key < 50:
            pkeys[1]=1
          elif x_key < 70:
            pkeys[22]=1
          elif x_key < 90:
            pkeys[2]=1
          elif x_key < 110:
            pkeys[3]=1
          elif x_key < 130:
            pkeys[23]=1
          elif x_key < 140:
            pkeys[4]=1
          elif x_key < 160:
            pkeys[24]=1
          elif x_key < 170:
            pkeys[5]=1
          elif x_key < 190:
            pkeys[25]=1
          elif x_key < 210:
            pkeys[6]=1
          elif x_key < 210+20:
            pkeys[7]=1
          elif x_key < 210+40:
            pkeys[26]=1
          elif x_key < 210+50:
            pkeys[8]=1
          elif x_key < 210+70:
            pkeys[27]=1
          elif x_key < 210+90:
            pkeys[9]=1
          elif x_key < 210+110:
            pkeys[10]=1
          elif x_key < 210+130:
            pkeys[28]=1
          elif x_key < 210+140:
            pkeys[11]=1
          elif x_key < 210+160:
            pkeys[29]=1
          elif x_key < 210+170:
            pkeys[12]=1
          elif x_key < 210+190:
            pkeys[30]=1
          elif x_key < 210+210:
            pkeys[13]=1
          if x_key < 420+20:
            pkeys[14]=1
          elif x_key < 420+40:
            pkeys[31]=1
          elif x_key < 420+50:
            pkeys[15]=1
          elif x_key < 420+70:
            pkeys[32]=1
          elif x_key < 420+90:
            pkeys[16]=1
          elif x_key < 420+110:
            pkeys[17]=1
          elif x_key < 420+130:
            pkeys[33]=1
          elif x_key < 420+140:
            pkeys[18]=1
          elif x_key < 420+160:
            pkeys[34]=1
          elif x_key < 420+170:
            pkeys[19]=1
          elif x_key < 420+190:
            pkeys[35]=1
          elif x_key < 420+210:
            pkeys[20]=1
        else:
          if x_key < 30:
            pkeys[0]=1
          elif x_key<60:
            pkeys[1]=1
          elif x_key<90:
            pkeys[2]=1
          elif x_key<120:
            pkeys[3]=1
          elif x_key<150:
            pkeys[4]=1
          elif x_key<180:
            pkeys[5]=1
          elif x_key<210:
            pkeys[6]=1
          elif x_key < 210+30:
            pkeys[7]=1
          elif x_key<210+60:
            pkeys[8]=1
          elif x_key<210+90:
            pkeys[9]=1
          elif x_key<210+120:
            pkeys[10]=1
          elif x_key<210+150:
            pkeys[11]=1
          elif x_key<210+180:
            pkeys[12]=1
          elif x_key<210+210:
            pkeys[13]=1
          elif x_key < 420+30:
            pkeys[14]=1
          elif x_key<420+60:
            pkeys[15]=1
          elif x_key<420+90:
            pkeys[16]=1
          elif x_key<420+120:
            pkeys[17]=1
          elif x_key<420+150:
            pkeys[18]=1
          elif x_key<420+180:
            pkeys[19]=1
          elif x_key<420+210:
            pkeys[20]=1
        #code for k array

        if cv2.waitKey(20) & 0xFF == ord('q'):
             break
    else:
        count=1
        prev_im = im
