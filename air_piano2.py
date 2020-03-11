import numpy as np
from time import sleep
import cv2
import time
from skimage.measure import compare_ssim
import argparse
import imutils

cap = cv2.VideoCapture(4)

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
        cv2.circle(frame, extTop, 8, (255, 0, 0), -1)
        cv2.imshow("Diff", frame)
        prev_im = im
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        count=1
        prev_im = im

