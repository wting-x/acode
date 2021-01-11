from PIL import Image
#获取图片指定像素点的像素
def getPngPix(img, pixelX, pixelY):
    str_strlist = img.load()
    data = str_strlist[pixelX,pixelY]
    return data

img_src = Image.open("image_01.png")
x = img_src.size[0]
y = img_src.size[1]
num = 0
for i in range(0,x):
    for j in range(0,y):
        t = getPngPix(img_src, i, j)
        if t[0]<=255 and t[0]>=200:
            if t[1]<=255 and t[1]>=200:
                    num+=1

print('经计算得，图中黄色部分的面积为',round(num/(x*y)*100,1),'%')
img_src.close()
