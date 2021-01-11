from collections import Counter
import numpy as np
import os
from PIL import Image
#from sklearn.preprocessing import LabelEncoder,OneHotEncoder
def createDataSet():
    #group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    group = [[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]]
    labels = ['A','A','B','B']
    return group, labels
def getDistances(inX,group):
    group=np.asarray(group)
    inX=np.tile(inX,(group.shape[0],1))-group
    inX=inX**2
    inX=inX.sum(axis=1)
    distances=inX**0.5
    '''
    distances=[0]*len(group)
    i=0

    for x,y in group:
        distances[i]=math.sqrt((inX[0]-x)**2+(inX[1]-y)**2)
        i+=1
    '''
    return distances
def getProbablity(data,k):#Compute Probability
    res=[]
    for x,y in data:
        res+=[y]
    sorteddata=res[:k]
    #print(Counter(d))
    #print(Counter(d).most_common(1)[0][0])
    return Counter(sorteddata).most_common(1)[0][0]
def myfile2matrix(FileName):
    Labels=[]
    try:
        infile=open(FileName,'r')
        numberOfLines = len(infile.readlines())
        infile=open(FileName,'r')
        Samples=np.zeros((numberOfLines,3))
        index=0
        while True:
            text_line = infile.readline()
            if text_line:
                #print(type(text_line), text_line)
                text_line=text_line.strip()
                rowlist=text_line.split('\t')
                #Samples+=[int(rowlist[:-1])]
                Samples[index]=rowlist[:-1]
                #label=rowlist[-1].rstrip('\n')
                Labels.append(int(rowlist[-1]))
                #print(Samples,Labels)
                index+=1
            else:
                break
    finally:
        infile.close()

    #labelencoder_Y = LabelEncoder()
    #Label =  labelencoder_Y.fit_transform(Labels)

    return Samples,Labels
#归一化特征值
def myAutoNorm(Samples):
    dataSet=np.zeros((Samples.shape))
    minvalues=np.amin(Samples,0)
    maxvalues=np.amax(Samples,0)
    x=np.divide((Samples-minvalues),(maxvalues-minvalues))
    return x
def myPng2vector(filename):
    returnVect = np.zeros(1024)
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[32*i+j] = int(lineStr[j])
    return returnVect

def myimg2vector(filename):
    returnVect = np.zeros(1024)
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[32*i+j] = int(lineStr[j])
    return returnVect
#先将文件转换成样本和标签
def mytxt2Matrix(filepath):
    filelist=os.listdir(filepath)
    #print(filelist)

    Samples=np.zeros((len(filelist),32*32))
    Labels=np.zeros(len(filelist))
    i=0
    for filename in filelist:
        Labels[i]=int(filename[0])
        allpathfilename=filepath+'\\'+filename
        Samples[i]=myimg2vector(allpathfilename)
        i+=1
    return Samples,Labels


def myHandWritingTest():
    #先将文件转换成样本和标签
    Samples,Labels=mytxt2Matrix('trainingDigits')
    testsamples,testlabels=mytxt2Matrix('testDigits')
    #loop call classify
    errorCount = 0.0
    for i in range(len(testlabels)):
        classifierResult=classify(testsamples[i,:],Samples,Labels,5)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult,testlabels[i]))
        if (classifierResult != testlabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(len(testlabels))))
    print (errorCount)
def LoadmyPic(filename):
    Img=Image.open(filename).convert('L')#转换成8位像素
    Img=Img.resize((32,32))
    imgarray=np.array(Img)
    rows,cols=imgarray.shape                #获取像素坐标（rows,cols）
    #二值化
    for i in range(rows):
        for j in range(cols):
            if imgarray[i,j]<=128:               #判断该点的值
                imgarray[i,j]=1
            else:
                imgarray[i,j]=0
    return imgarray

def myselfDigitTest(filename):
    Samples,Labels=mytxt2Matrix('trainingDigits')
    dataSet=LoadmyPic(filename)
    dataSet=np.reshape(dataSet,1024)
    result=classify(dataSet,Samples,Labels,15)
    print(result)

def datingClassTest():
    hoRatio = 0.10      #hold out 10%
    datingDataMat,datingLabels = myfile2matrix('datingTestSet2.txt')       #load data setfrom file
    #normMat, ranges, minVals = myAutoNorm(datingDataMat)
    normMat = myAutoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult = classify(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print ("the total error rate is: %f" % (errorCount/float(numTestVecs)))
    print (errorCount)
'''
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges, (m,1))   #element wise divide
    return normDataSet, ranges, minVals
'''
def classify(inX,group,labels,k):
    #Compute Distances
    distances=getDistances(inX,group)
    #sort array
    distancetuple=zip(distances,labels)
    distances=[]
    for x,y in distancetuple:
        distances.append([x,y])
    #Sort
    distances.sort()
    #Compute Probability
    result=getProbablity(distances,k)
    return result

#myHandWritingTest()
'''
Samples,Labels=mytxt2Matrix('trainingDigits')
print(Samples[0,0:32])
print(Labels[0])
'''
'''
import matplotlib
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(Samples[:1],Samples[:2])
'''
'''
group,labels=createDataSet()
result=classify([10,10],group,labels,3)
print(result)
'''
'''
Samples,Labels=myfile2matrix('datingTestSet2.txt')

print(Samples)
print('-----------------------')
print(Labels)

Samples=myAutoNorm(Samples)
print(Samples)

datingClassTest()
'''
'''
for i in range(10):
    #str='E:\\MyDigits\\My_1_%d.jpg'%(i)
    str=r'E:\MyDigits\data\%d.png'%(i)
    myselfDigitTest(str)
'''
#myselfDigitTest(r'E:\MyDigits\7.jpg')

