import numpy as np

# 构建数据
def creatDataSet():
    #  喜剧片  科幻片  爱情片 动作片
    group = np.array([[3,10,23,114],
                      [2,5,23,160],
                      [1,9,8,154],
                      [101,10,12,11],
                      [99,5,7,8,],
                      [98,2,10,5],
                      [4,99,14,10],
                      [6,100,11,23],
                      [9,100,1,1],
                      [1,4,99,3],
                      [4,5,78,6],
                      [1,4,88,9]])
    labels = ["动作片","动作片","动作片","喜剧片","喜剧片","喜剧片","科幻片","科幻片","科幻片","爱情片","爱情片","爱情片"]
    return group, labels

def classify(input, dataSet, labels, k):
    # 获得样本的行数
    dataSize = dataSet.shape[0]
    print(dataSet.shape[0])
    # 利用欧式距离公式计算距离
    # nump.tile() 就是把数组沿各个方向复制
    print(input)
    kdiff = np.tile(input, (dataSize, 1)) - dataSet
    sqdiff = kdiff**2
    # 行向量分别相加，从而得到新的一个行向量
    sqnumdiff = np.sum(sqdiff, axis=1)
    dist = sqnumdiff**0.5
    # 将距离进行排序
    soreDistIndex = np.argsort(dist)
    classCount = {}
    for i in range(k):
        print(soreDistIndex[i])
        voteLabel = labels[soreDistIndex[i]]
        print(voteLabel)
        # 对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    # 选取出现的类别次数最多的类别
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key

    return classes

if __name__ == "__main__":
    dataSet, labels = creatDataSet()
    # 测试数据
    input = np.array([9,90,500,4])
    k = 3
    output = classify(input, dataSet, labels, k)
    print("测试数据为:", input, "分类结果为：", output)
