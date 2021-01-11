# coding=gbk
"""
���Խ�Sobel��Ե�ͻ�����ɫHSV�����ֶ�λ��������ɸѡ��ʵ�ֳ��ƶ�λ
14/50
"""

import cv2 as cv
import numpy as np

def location(img_resize):
    #��˹ģ��+��ֵ�˲�
    img_gaus = cv.GaussianBlur(img_resize,(5,5),0)          #��˹ģ��
    img_med = cv.medianBlur(img_gaus,5)                     #��ֵ�˲�
    #HSVģ�ʹ���ֱ����ֵ��
    #ת��ΪHSVģ��
    img_hsv = cv.cvtColor(img_med,cv.COLOR_BGR2HSV)        #hsvģ��
    lower_blue = np.array([90,40,50])
    higher_blue = np.array([150,255,255])
    mask = cv.inRange(img_hsv,lower_blue,higher_blue)    #��Ĥ����
    img_res = cv.bitwise_and(img_med,img_med,mask=mask)
    #�ҶȻ�+��ֵ��
    img_gray_h = cv.cvtColor(img_res,cv.COLOR_BGR2GRAY)    #ת���˻ҶȻ�
    ret1,img_thre_h = cv.threshold(img_gray_h,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    #����Sobel�������㣬ֱ����ֵ��
    img_gray_s = cv.cvtColor(img_med,cv.COLOR_BGR2GRAY)
    #sobel��������
    img_sobel_x = cv.Sobel(img_gray_s,cv.CV_32F,1,0,ksize=3)    #x��Sobel����
    img_sobel_y = cv.Sobel(img_gray_s,cv.CV_32F,0,1,ksize=3)
    img_ab_y = np.uint8(np.absolute(img_sobel_y))
    img_ab_x = np.uint8(np.absolute(img_sobel_x))               #���ص�ȡ����ֵ
    img_ab = cv.addWeighted(img_ab_x, 0.5, img_ab_y, 0.5,0)   #������ͼ�������һ�𣨰�һ��Ȩֵ��
    #�����ټ�һ�θ�˹ȥ��
    img_gaus_1 = cv.GaussianBlur(img_ab,(5,5),0)          #��˹ģ��

    #��ֵ������
    ret2,img_thre_s = cv.threshold(img_gaus_1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)     #����ֵ��

	#��ɫ�ռ����Ե���ӵ�ͼ����ɸѡ
    #ͬʱ����������ֵͼƬ�������߾�Ϊ255������255
    img_1 = np.zeros(img_thre_h.shape,np.uint8)  #���¿���ͼƬ
    height = img_resize.shape[0]    #����
    width = img_resize.shape[1]     #����

    for i in range(height):
        for j in range(width):
            h = img_thre_h[i][j]
            s = img_thre_s[i][j]
            if h ==255 and s ==255 :
                img_1[i][j] = 255
            else:
                img_1[i][j] = 0
    #cv.imshow('threshold',img_1)
    #cv.waitKey(0)
    #��ֵ�����ͼ����бղ���

    kernel = np.ones((14,18),np.uint8)
    img_close = cv.morphologyEx(img_1,cv.MORPH_CLOSE,kernel)    #�ղ���
    img_med_2 = cv.medianBlur(img_close,5)
    #cv.imshow('close',img_med_2)
    #cv.waitKey(0)

    #��������
    regions = []         #����
    list_rate = []
    img_input = img_med_2.copy()

    contours,hierarchy = cv.findContours(img_input,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    #   ɸѡ�����С��
    for contour in contours:
        #��������������
        area = cv.contourArea(contour)
        #���С�Ķ�ɸѡ��
        if area < 500 or area >5000:
            continue
        #��������,epsilon���Ǵ����������������������롣��һ��׼ȷ�ʲ������õ�epsilon��ѡ����Եõ���ȷ�������True���������Ƿ�պϡ�
        #�ҵ���С�ľ��Σ��þ��ο����з���
        rect = cv.minAreaRect(contour)
        #box���ĸ��������
        box = cv.boxPoints(rect)
        box = np.int0(box)
        #����ߺͿ�
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        #������������³��߱�Ϊ2-5֮�䣨��ȷһ���Ϊ��2.2,3.6����
        ratio = float(width) / float(height)
        if ratio > 2 and ratio < 5:
            regions.append(box)
            list_rate.append(ratio)

    #������Ƶ�����
    print('[INF0]:Detect %d license plates' % len(regions))    #������Ƴ���ͼ�������
    if len(regions)>0:
        #�ú��߻�����Щ�ҵ�������
        cv.drawContours(img_resize, regions, -1, (0, 0, 255), 1)
        cv.imshow('result',img_resize)
        cv.waitKey(0)

if __name__ == "__main__":
    img = cv.imread('D:/acode/Python/GetLisence/img/mi52020/IMG_ (1).jpg')     #�����Լ���ͼƬ
    if img.shape[0]<=img.shape[1]:
        img_resize = cv.resize(img,(800,600),)
    else:
        img_resize = cv.resize(img,(600,800),)
    location(img_resize)