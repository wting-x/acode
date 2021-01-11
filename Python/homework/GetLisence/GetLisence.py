# coding=gbk
"""
尝试将Sobel边缘和基于颜色HSV的两种定位方法互相筛选，实现车牌定位
14/50
"""

import cv2 as cv
import numpy as np

def location(img_resize):
    #高斯模糊+中值滤波
    img_gaus = cv.GaussianBlur(img_resize,(5,5),0)          #高斯模糊
    img_med = cv.medianBlur(img_gaus,5)                     #中值滤波
    #HSV模型处理，直至二值化
    #转换为HSV模型
    img_hsv = cv.cvtColor(img_med,cv.COLOR_BGR2HSV)        #hsv模型
    lower_blue = np.array([90,40,50])
    higher_blue = np.array([150,255,255])
    mask = cv.inRange(img_hsv,lower_blue,higher_blue)    #掩膜操作
    img_res = cv.bitwise_and(img_med,img_med,mask=mask)
    #灰度化+二值化
    img_gray_h = cv.cvtColor(img_res,cv.COLOR_BGR2GRAY)    #转换了灰度化
    ret1,img_thre_h = cv.threshold(img_gray_h,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    #进行Sobel算子运算，直至二值化
    img_gray_s = cv.cvtColor(img_med,cv.COLOR_BGR2GRAY)
    #sobel算子运算
    img_sobel_x = cv.Sobel(img_gray_s,cv.CV_32F,1,0,ksize=3)    #x轴Sobel运算
    img_sobel_y = cv.Sobel(img_gray_s,cv.CV_32F,0,1,ksize=3)
    img_ab_y = np.uint8(np.absolute(img_sobel_y))
    img_ab_x = np.uint8(np.absolute(img_sobel_x))               #像素点取绝对值
    img_ab = cv.addWeighted(img_ab_x, 0.5, img_ab_y, 0.5,0)   #将两幅图像叠加在一起（按一定权值）
    #考虑再加一次高斯去噪
    img_gaus_1 = cv.GaussianBlur(img_ab,(5,5),0)          #高斯模糊

    #二值化操作
    ret2,img_thre_s = cv.threshold(img_gaus_1,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)     #正二值化

	#颜色空间与边缘算子的图像互相筛选
    #同时遍历两幅二值图片，若两者均为255，则置255
    img_1 = np.zeros(img_thre_h.shape,np.uint8)  #重新拷贝图片
    height = img_resize.shape[0]    #行数
    width = img_resize.shape[1]     #列数

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
    #二值化后的图像进行闭操作

    kernel = np.ones((14,18),np.uint8)
    img_close = cv.morphologyEx(img_1,cv.MORPH_CLOSE,kernel)    #闭操作
    img_med_2 = cv.medianBlur(img_close,5)
    #cv.imshow('close',img_med_2)
    #cv.waitKey(0)

    #查找轮廓
    regions = []         #区域
    list_rate = []
    img_input = img_med_2.copy()

    contours,hierarchy = cv.findContours(img_input,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    #   筛选面积最小的
    for contour in contours:
        #计算该轮廓的面积
        area = cv.contourArea(contour)
        #面积小的都筛选掉
        if area < 500 or area >5000:
            continue
        #轮廓近似,epsilon，是从轮廓到近似轮廓的最大距离。是一个准确率参数，好的epsilon的选择可以得到正确的输出。True决定曲线是否闭合。
        #找到最小的矩形，该矩形可能有方向
        rect = cv.minAreaRect(contour)
        #box是四个点的坐标
        box = cv.boxPoints(rect)
        box = np.int0(box)
        #计算高和宽
        height = abs(box[0][1] - box[2][1])
        width = abs(box[0][0] - box[2][0])
        #车牌正常情况下长高比为2-5之间（精确一点可为（2.2,3.6））
        ratio = float(width) / float(height)
        if ratio > 2 and ratio < 5:
            regions.append(box)
            list_rate.append(ratio)

    #输出车牌的轮廓
    print('[INF0]:Detect %d license plates' % len(regions))    #输出疑似车牌图块的数量
    if len(regions)>0:
        #用红线画出这些找到的轮廓
        cv.drawContours(img_resize, regions, -1, (0, 0, 255), 1)
        cv.imshow('result',img_resize)
        cv.waitKey(0)

if __name__ == "__main__":
    img = cv.imread('D:/acode/Python/GetLisence/img/mi52020/IMG_ (1).jpg')     #输入自己的图片
    if img.shape[0]<=img.shape[1]:
        img_resize = cv.resize(img,(800,600),)
    else:
        img_resize = cv.resize(img,(600,800),)
    location(img_resize)