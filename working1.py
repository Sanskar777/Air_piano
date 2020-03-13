import numpy as np
from time import sleep
import cv2
import time
from skimage.measure import compare_ssim
import argparse
import imutils
# from pygame import mixer
#from playsound import playsound
import threading
import pyaudio
import wave
import sys

lock =np.zeros(36)
thread_string=[]
data=[]
stream=[]
wf=[]
p = pyaudio.PyAudio()
CHUNK=1024

for i in range(36):
    thread_string.append('t'+str(i))
    data.append('data'+str(i))
    stream.append('stream'+str(i))
    wf.append('wf'+str(i))

def play_music(i):
    wf[i] = wave.open(str(i+1)+'.wav','rb')
    stream[i] = p.open(format=p.get_format_from_width(wf[i].getsampwidth()),
                        channels=wf[i].getnchannels(),
                        rate=wf[i].getframerate(),
                        output=True)
    data[i] = wf[i].readframes(CHUNK)
    while len(data[i]) > 0:
        stream[i].write(data[i])
        data[i] = wf[i].readframes(CHUNK)
    stream[i].stop_stream()
    stream[i].close()
    lock[i]=0
    return

count=0
if __name__ == '__main__' :
    cap = cv2.VideoCapture(1)
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        frame = cv2.flip(frame,0)
        im = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if count%3==1:
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
            # cv2.imshow("Original", grayA)
            # cv2.imshow("Modified", grayB)

            # cv2.imshow("Thresh", thresh)

            c = max(cnts, key=cv2.contourArea)
            #extLeft = tuple(c[c[:, :, 0].argmin()][0])
            #extRight = tuple(c[c[:, :, 0].argmax()][0])
            extTop = tuple(c[c[:, :, 1].argmin()][0])
            #cv2.circle(frame, extLeft, 8, (0, 0, 255), -1)
            #cv2.circle(frame, extRight, 8, (0, 255, 0), -1)
            cv2.circle(frame, extTop, 8, (255, 0, 0), -1)

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
            # cv2.imshow("Diff1", frame)
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
            cv2.imshow("Diff", frame)
            pkeys=np.zeros(36)
            x_key = extTop[0]
            y_key = extTop[1]
            if y_key < (y0+100) and y_key>150:
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
              elif x_key < 420+20:
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
            elif y_key>(y0+100):
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

            for i in range(len(pkeys)):
                if pkeys[i]>0:
                    # print (str(i)+ " key is active")
                    if lock[i]==0:
                        lock[i]=1
                        print (str(i)+ " key is active")
                        thread_string[i] = threading.Thread(target=play_music,args=(i,))
                        thread_string[i].start()
                        #thread_string[i].join()
                        # lock[i]=0
                    else:
                        print ('key in use')
                    # mixer.init()
                    # playsound(str(i)+'.mp3')
                    # mixer.music.play()

            # cv2.imshow("Diff", frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                 break
        else:
            count=count+1
            prev_im = im
