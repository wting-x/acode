import cv2
import numpy as np
import matplotlib.pyplot as plt

def Origin_histogram( img ):
    #建立原始图像各灰度级的灰度值与像素个数对应表
    histogram = {}
    for i in range( img.shape[0] ):
        for j in range( img.shape[1] ):
            k = img[i][j]
            if k in histogram:
                histogram[k] += 1
            else:
                histogram[k] = 1

    sorted_histogram = {}#建立排好序的映射表
    sorted_list = sorted( histogram )#根据灰度值进行从低至高的排序

    for j in range( len( sorted_list ) ):
        sorted_histogram[ sorted_list[j] ] = histogram[ sorted_list[j] ]

    return sorted_histogram

def equalization_histogram( histogram, img ):

    pr = {}#建立概率分布映射表

    for i in histogram.keys():
        pr[i] = histogram[i] / ( img.shape[0] * img.shape[1] )

    tmp = 0
    for m in pr.keys():
        tmp += pr[m]
        pr[m] =  max( histogram ) * tmp

    new_img = np.zeros( shape = ( img.shape[0], img.shape[1] ), dtype = np.uint8 )

    for k in range( img.shape[0] ):
        for l in range( img.shape[1] ):
            new_img[k][l] = pr[img[k][l]]

    return new_img

def GrayHist( img ):
    # 计算灰度直方图
    height, width = img.shape[:2]
    grayHist = np.zeros([256], np.uint64)
    for i in range(height):
        for j in range(width):
            grayHist[img[i][j]] += 1
    return grayHist

if __name__ == '__main__':
    #读取原始图像
    img = cv2.imread( 'homework_boy_hist.png', cv2.IMREAD_GRAYSCALE )
    #计算原图灰度直方图
    origin_histogram = Origin_histogram( img )
    #直方图均衡化
    new_img = equalization_histogram( origin_histogram, img )

    origin_grayHist = GrayHist(img)
    equaliza_grayHist = GrayHist( new_img )
    x = np.arange(256)

    # 绘制灰度直方图
    plt.figure(figsize=(8, 10))
    plt.subplot( 2, 2, 1 )
    plt.plot(x, origin_grayHist, 'r', linewidth=2, c='black')
    plt.title("Origin")

    plt.subplot( 2, 2, 2 )
    plt.plot(x, equaliza_grayHist, 'r', linewidth=2, c='black')
    plt.title("Equalization")

    plt.subplot( 2, 2, 3 )
    plt.imshow( img, cmap = plt.cm.gray )
    plt.title( 'Origin' )

    plt.subplot( 2, 2, 4 )
    plt.imshow( new_img, cmap = plt.cm.gray )
    plt.title("Equalization")
    plt.show()