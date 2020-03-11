import numpy as np
from time import sleep
import cv2
import time
from skimage.measure import compare_ssim
import argparse
import imutils

cap = cv2.VideoCapture(1)

count=0
while(True):
    ret, frame = cap.read()
    im = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if count==1:
        grayA = prev_im
        grayB = im
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))
        thresh = cv2.threshold(diff, 0, 255,
        cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cv2.imshow("Original", imageA)
        cv2.imshow("Modified", imageB)

        cv2.imshow("Thresh", thresh)

        c = max(cnts, key=cv2.contourArea)
        extLeft = tuple(c[c[:, :, 0].argmin()][0])
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])
        cv2.circle(diff, extLeft, 8, (0, 0, 255), -1)
        cv2.circle(diff, extRight, 8, (0, 255, 0), -1)
        cv2.circle(diff, extTop, 8, (255, 0, 0), -1)
        cv2.imshow("Diff", diff)
        prev_im = im
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        count=1
        prev_im = im


# while(True):
#
#     ret, frame = cap.read()
#     frame=cv2.flip(frame,1)
#     s = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame', s)
#     blurred_img = cv2.blur(s, (3, 3))
#     # edges = cv2.createBackgroundSubtractorMOG2().apply(blurred_img)
#     ret,edges = cv2.threshold(blurred_img,120,255,cv2.THRESH_BINARY)
#     edges = cv2.Canny(blurred_img,70,140)
#
#     ret,thresholded_img = cv2.threshold(edges,120,255,cv2.THRESH_BINARY)
#     cv2.imshow('showing the edges', thresholded_img)
#     contour,heirarchy = cv2.findContours(thresholded_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#     areas = [cv2.contourArea(c) for c in contour]
#     index = np.argmax(areas)
#     largest_contour = contour[index]
#     # drawing = np.zeros((thresholded_img.shape[0],thresholded_img.shape[1],1),np.uint8)
#     cv2.drawContours(thresholded_img,contour,-1,(255,0,0),3)
#     cv2.imshow('drawing the hand', thresholded_img)
#     # contour_list = contours(thresholded_img)
#
#     ###################################
#
#     ###################################
#     try:
#         contour,heirarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#         # areas = [cv2.contourArea(c) for c in contour]
#         # # index = np.argmax(areas)q
#         # max_area=0
#         # second_lar_area=0
#         # if len(areas)>1:
#         #     for j in range(len(areas)):
#         #         if areas[j]>max_area:
#         #             max_index = j
#         #             max_area = areas[j]
#         #         if areas[j]>=second_lar_area and areas[j]<=max_area:
#         #             second_max_index = j
#         #             second_lar_area = areas[j]
#         #     largest_contour_index_list = []
#         #     largest_contour_index_list.append(max_index)
#         #     largest_contour_index_list.append(second_max_index)
#         # if len(largest_contour_index_list)>1:
#         #     largest_contour = contour[largest_contour_index_list[0]]
#         #     cv2.drawContours(frame,contour,largest_contour_index_list[0],(255,0,0),3)
#         #     cv2.drawContours(frame,contour,largest_contour_index_list[1],(255,0,0),3)
#         #     cv2.imshow('showing hand contour', frame)
#         hull_list=[]
#         for j in range(len(contour)):
#             moments = cv2.moments(contour[j])
#             cnt = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
#             hull= cv2.convexHull(contour[j],returnPoints = False)
#             # for j in range(len(hull_list)):
#             defects = cv2.convexityDefects(contour[j],hull)
#             for i in range(defects.shape[0]):
#                 st,e,f,d = defects[i,0]
#                 start = tuple(largest_contour[st][0])
#                 end = tuple(largest_contour[e][0])
#                 far = tuple(largest_contour[f][0])
#                 cv2.line(frame,start,end,[0,255,0],2)
#                 cv2.circle(frame,far,5,[0,255,255],-1)
#                 # defects2 = cv2.convexityDefects(contour[largest_contour_index_list[1]],hull2)
#                 # for i in range(defects2.shape[0]):
#                 #     st,e,f,d = defects2[i,0]
#                 #     start = tuple(largest_contour[st][0])
#                 #     end = tuple(largest_contour[e][0])
#                 #     far = tuple(largest_contour[f][0])
#                 #     cv2.line(frame,start,end,[0,255,0],2)
#                 #     cv2.circle(frame,far,5,[0,255,255],-1)
#                 cv2.imshow('showing finger tips',frame)
#         if cv2.waitKey(20) & 0xFF == ord('q'):
#             break
#     except:
#         if cv2.waitKey(20) & 0xFF == ord('q'):
#             break
#
# cap.release()
# cv2.destroyAllWindows()
#
# # def calc_roc(img):
# #     i=1
# #     j=1
# #     kernel = [[-1,-2,1],[2,3,-2],[1,2,-1]]
# #     derivative = np
# #     for i in range(img.shape[0]-2):
# #         for  j in range(img.shape[1]-2):
# #             derivative[i][j] = img[i][j]*kernel[1][1] + img[i-1][j-1]*kernel[0][0]+\
# #             img[i-1][j]*kernel[0][1]+img[i-1][j+1]*kernel[0][2]+img[i][j-1]*\
# #             kernel[1][0]+img[i][j+1]*kernel[1][2]+img[i+1][j-1]*kernel[2][0]+\
# #             img[i+1][j]*kernel[2][1]+img[i+1][j+1]*kernel[2][2]
