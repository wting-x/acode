import cv2
img=cv2.imread('test.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('one.png',img)
import numpy as np

from PIL import Image

import scipy.signal as signal



im = Image.open('one.png')

data = []

width, height = im.size



# 读取图像像素值

for h in range(height):

    row = []

    for w in range(width):

        value = im.getpixel((w,h))

        row.append(value)

    data.append(row)



# 二维中值滤波

data = np.float32(data)

# 滤波窗口的大小会对结果产生很大影响

data = signal.medfilt2d(data, (7,7))



# 创建并保存结果图像

for h in range(height):

    for w in range(width):

        im.putpixel((w,h), int(data[h][w]))



im.save('result.jpg')