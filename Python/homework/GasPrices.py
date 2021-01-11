import numpy as np

def Yearly_Average(dict):
    price = []  #每一年的价格的列表
    year = 1993
    #逐年求年平均价格
    for d, p in dict.items():
        if year != d[2]:
            average = np.mean(price)
            print(year,':%.3f'%average)
            price.clear()
            year = d[2]
        price.append(p)
    average = np.mean(price)
    print(year,':%.3f'%average)

def Monthly_Average(dict):
    price = []  #当年每个月的价格的列表
    year = 1993
    month = 1

    #逐年逐月求年平均价格
    for d, p in dict.items():
        #到下一年或者下一个月时
        if year != d[2] or month != d[0]:
            if len(price) != 0:
                average = np.mean(price)
                print(year,'-',month,'\t%.3f'%average)
            price.clear()
            if year!= d[2]:
                print('\n')
                year = d[2]
            month = d[0]

        price.append(p)
    #循环结束

    average = np.mean(price)
    print(year,'-',month,'\t%.3f'%average)

def Yearly_Highest_Lowest(dict):
    year = 1993
    high_date = []  #年最高价格日期的列表
    high = 0    #年最高价格
    low_date = []   #年最低价格日期的列表
    low = 100   #年最低价格

    #遍历字典的键和值
    for d, p in dict.items():
        if year!=d[2]:
            print(year,'\nHIGHPRICE:',high,'\tHIGHDATE:',high_date)
            print('LOWPRICE:',low,'\tLOWDATE:',low_date,'\n')
            year = d[2]
            high_date.clear()
            high = 0
            low_date.clear()
            low = 100

        if p>high:
            high = p
            high_date.clear()
            high_date.append(d[3])
        elif p==high:
            high_date.append(d[3])

        if p<low:
            low = p
            low_date.clear()
            low_date.append(d[3])
        elif p==low:
            low_date.append(d[3])
    print(year,'\nHIGHPRICE:',high,'\tHIGHDATE:',high_date)
    print('LOWPRICE:',low,'\tLOWDATE:',low_date,'\n')

def Sort_LowToHigh(dict):
    price = []
    line = []
    i=0
    for d, p in dict.items():
        price.append(p)
        line.append(d[4])
    dist = np.argsort(price)
    f_LTH=open(r'D:\GasPrice_LTH.txt','a')
    f_LTH.seek(0)
    f_LTH.truncate()   #清空文件

    for i in range(0,len(line)):
        f_LTH.write(line[dist[i]])
        i+=1

    f_LTH.close()

def Sort_HighToLow(dict):
    price = []
    line = []
    i=0
    for d, p in dict.items():
        price.append(p)
        line.append(d[4])
    dist = np.argsort(price)
    f_LTH=open(r'D:\GasPrice_HTL.txt','a')
    f_LTH.seek(0)
    f_LTH.truncate()   #清空文件

    for i in range(0,len(line)):
        j=len(line)-i-1
        f_LTH.write(line[dist[j]])
        i+=1

    f_LTH.close()

def Choose(dict):
    print("请用序号输入您想要进行的操作")
    print("1：计算每年天然气的平均价格")
    print("2：计算每月天然气的平均价格")
    print("3：计算每年天然气的最低价格和最高价格及对应日期")
    print("4：生成一个文本文件GasPrice_LTH.txt列出从低到高的价格以及日期")
    print("5：生成一个文本文件GasPrice_HTL.txt列出从高到低的价格以及日期")
    print("6：结束操作")
    while 1:
        options = (int)(input())
        if options == 1:Yearly_Average(dict)
        elif options == 2:Monthly_Average(dict)
        elif options == 3:Yearly_Highest_Lowest(dict)
        elif options == 4:Sort_LowToHigh(dict)
        elif options == 5:Sort_HighToLow(dict)
        elif options == 6:break
        else:print("操作错误")
        print("请再次输入操作：")

def main():
    #打开文件，创建日期与价格的字典
    input_txt = 'D:/GasPrices.txt'
    f = open(input_txt)
    dict = {}

    #行遍历，创建字典
    for line in f:
        try:
            str = line.strip('\n')
            str = line.split(':')

            date = str[0]
            date = date.split('-')
            date = [int(x) for x in date]
            date.append(str[0])
            date.append(line)
            date = (tuple)(date)
            price = (float)(str[1])

            dict[date] = price
        except IndexError as s:
            pass
    #循环结束
    f.close()
    Choose(dict)

if __name__ == "__main__":
    main()