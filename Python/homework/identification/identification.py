import cv2
import numpy as np
import os
import MykNN
WIDTH=HIGHT=32
def myimg2vector(filename):
    img=cv2.imread(filename)
    #print(img.shape)
    img=cv2.resize(img,(WIDTH,HIGHT))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化
    # 2、将灰度图像二值化，设定阈值是100
    ret, img_binary=cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

    #print(img_binary.shape)
    '''
    cv2.imshow('resize',img_binary)
    cv2.waitKey()
    cv2.destroyAllWindows()
    '''
    img_binary=np.reshape(img_binary,(WIDTH*HIGHT))
    #img_binary.reshape(WIDTH*HIGHT)
    #print(img_binary.shape)
    return img_binary
#先将文件转换成样本和标签
def FilePath2Matrix(filepath):
    filelist=os.listdir(filepath)
    #print(filelist)

    Samples=np.zeros((len(filelist),32*32))
    #Labels=np.zeros(len(filelist))
    Labels=[]
    i=0
    for filename in filelist:
        preName=filename[:filename.index('_')]
        Labels.append(preName)
        allpathfilename=filepath+'\\'+filename
        Samples[i]=myimg2vector(allpathfilename)
        i+=1
    return Samples,Labels
def myselfDigitTest(filename):
    Samples,Labels=FilePath2Matrix(r'D:\acode\Python\identification\MyDigits')
    dataSet=myimg2vector(filename)
    #dataSet=np.reshape(dataSet,WIDTH*HIGHT)
    result=MykNN.classify(dataSet,Samples,Labels,1)
    print(result)

print('----------')
'''
Samples,Labels=FilePath2Matrix(r'D:\acode\Python\identification\MyDigits')
print(Samples.shape)
print(len(Labels))
'''
#车牌号有7个字符
Num=7
for i in range(7):
    str='%d.jpg'%(i)
    myselfDigitTest(str)
