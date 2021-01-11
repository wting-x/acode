import cv2 as cv
import numpy as np

def resize_img(img, max_size):
    """ resize图像 """
    h, w = img.shape[0:2]
    scale = max_size / max(h, w)
    img_resized = cv.resize(img, None, fx=scale, fy=scale,
                            interpolation=cv.INTER_CUBIC)
    # print(img_resized.shape)
    return img_resized


def stretching(img):
    """ 图像拉伸 """
    maxi = float(img.max())
    mini = float(img.min())

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = 255 / (maxi - mini) * img[i, j] - (255 * mini) / (maxi - mini)
    img_stretched = img
    return img_stretched


def absdiff(img):
    """ 对开运算前后图像做差分 """
    # 进行开运算，用来去除噪声
    r = 15
    h = w = r * 2 + 1
    kernel = np.zeros((h, w), np.uint8)
    cv.circle(kernel, (r, r), r, 1, -1)
    # 开运算
    img_opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    # 获取差分图
    img_absdiff = cv.absdiff(img, img_opening)
    return img_absdiff


def binarization(img):
    """ 二值化处理函数 """
    maxi = float(img.max())
    mini = float(img.min())
    x = maxi - ((maxi - mini) / 2)
    # 二值化, 返回阈值ret和二值化操作后的图像img_binary
    ret, img_binary = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    # img_binary = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 5, 2)
    # 返回二值化后的黑白图像
    return img_binary


def canny(img):
    """ canny边缘检测 """
    img_canny = cv.Canny(img, img.shape[0], img.shape[1])
    return img_canny


def opening_closing(img):
    """ 开闭运算，保留车牌区域，消除其他区域，从而定位车牌 """
    # 进行闭运算
    kernel = np.ones((5, 23), np.uint8)
    img_closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

    # 进行开运算
    img_opening1 = cv.morphologyEx(img_closing, cv.MORPH_OPEN, kernel)

    # 再次进行开运算
    kernel = np.ones((11, 6), np.uint8)
    img_opening2 = cv.morphologyEx(img_opening1, cv.MORPH_OPEN, kernel)
    return img_opening2


def find_rectangle(contour):
    """ 寻找矩形轮廓 """
    y, x = [], []
    for p in contour:
        y.append(p[0][0])
        x.append(p[0][1])
    return [min(y), min(x), max(y), max(x)]


def locate_license(original, img):
    """ 定位车牌号 """
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    img_cont = original.copy()
    img_cont = cv.drawContours(img_cont, contours, -1, (255, 0, 0), 6)
    # 计算轮廓面积及高宽比
    block = []
    for c in contours:
        # 找出轮廓的左上点和右下点，由此计算它的面积和长度比
        r = find_rectangle(c)    # 里面是轮廓的左上点和右下点
        a = (r[2] - r[0]) * (r[3] - r[1])   # 面积
        s = (r[2] - r[0]) / (r[3] - r[1])   # 长度比
        block.append([r, a, s])
    # 选出面积最大的五个区域
    block = sorted(block, key=lambda bl: bl[1])[-5:]

    # 使用颜色识别判断找出最像车牌的区域
    maxweight, maxindex=0, -1
    for i in range(len(block)):
        # print('block', block[i])
        if 2 <= block[i][2] <=4 and 1000 <= block[i][1] <= 20000:    # 对矩形区域高宽比及面积进行限制
            b = original[block[i][0][1]: block[i][0][3], block[i][0][0]: block[i][0][2]]
            # BGR转HSV
            hsv = cv.cvtColor(b, cv.COLOR_BGR2HSV)
            lower = np.array([100, 50, 50])
            upper = np.array([140, 255, 255])
            # 根据阈值构建掩膜
            mask = cv.inRange(hsv, lower, upper)
            # 统计权值
            w1 = 0
            for m in mask:
                w1 += m / 255

            w2 = 0
            for n in w1:
                w2 += n

            # 选出最大权值的区域
            if w2 > maxweight:
                maxindex = i
                maxweight = w2

    rect = block[maxindex][0]
    return rect


def preprocessing(img):
    # resize图像至300 * 400
    img_resized = resize_img(img, 400)
    # 转灰度图
    img_gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)
    # 高斯滤波
    # img_gaussian = cv.GaussianBlur(img_gray, (3,3), 0)
    # cv.imshow("Gaussian_Blur", img_gaussian)
    # 灰度拉伸，提升图像对比度
    img_stretched = stretching(img_gray)
    # 差分开运算前后图像
    img_absdiff = absdiff(img_stretched)
    # 图像二值化
    img_binary = binarization(img_absdiff)
    # 边缘检测
    img_canny = canny(img_binary)
    # 开闭运算，保留车牌区域，消除其他区域
    img_opening2 = opening_closing(img_canny)
    # 定位车牌号所在矩形区域
    rect = locate_license(img_resized, img_opening2)
    print("rect:", rect)
    # 框出并显示车牌
    img_copy = img_resized.copy()
    cv.rectangle(img_copy, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    cv.imshow('License', img_copy)
    return rect, img_resized


def cut_license(original, rect):
    """ 裁剪车牌 """
    license_img = original[rect[1]:rect[3], rect[0]:rect[2]]
    return license_img


def find_waves(threshold, histogram):
    """ 根据设定的阈值和图片直方图，找出波峰，用于分隔字符 """
    up_point = -1    # 上升点
    is_peak = False
    if histogram[0] > threshold:
        up_point = 0
        is_peak = True
    wave_peaks = []
    for i, x in enumerate(histogram):
        if is_peak and x < threshold:
            if i - up_point > 2:
                is_peak = False
                wave_peaks.append((up_point, i))
        elif not is_peak and x >= threshold:
            is_peak = True
            up_point = i
    if is_peak and up_point != -1 and i - up_point > 4:
        wave_peaks.append((up_point, i))
    return wave_peaks


def remove_upanddown_border(img):
    """ 去除车牌上下无用的边缘部分，确定上下边界 """
    plate_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, plate_binary_img = cv.threshold(plate_gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    row_histogram = np.sum(plate_binary_img, axis=1)    # 数组的每一行求和
    row_min = np.min(row_histogram)
    row_average = np.sum(row_histogram) / plate_binary_img.shape[0]
    row_threshold = (row_min + row_average) / 2
    wave_peaks = find_waves(row_threshold, row_histogram)
    # 挑选跨度最大的波峰
    wave_span = 0.0
    selected_wave = []
    for wave_peak in wave_peaks:
        span = wave_peak[1] - wave_peak[0]
        if span > wave_span:
            wave_span = span
            selected_wave = wave_peak
    plate_binary_img = plate_binary_img[selected_wave[0]:selected_wave[1], :]
    return  plate_binary_img


def find_end(start, arg, black, white, width, black_max, white_max):
    end = start + 1
    for m in range(start + 1, width - 1):
        if (black[m] if arg else white[m]) > (0.95*black_max if arg else 0.95*white_max):
            end = m
            break
    return end


def char_segmentation(thresh):
    """ 分割字符 """
    white, black = [], []    # list记录每一列的黑/白色像素总和
    height, width = thresh.shape
    white_max = 0    # 仅保存每列，取列中白色最多的像素总数
    black_max = 0    # 仅保存每列，取列中黑色最多的像素总数
    # 计算每一列的黑白像素总和
    for i in range(width):
        line_white = 0    # 这一列白色总数
        line_black = 0    # 这一列黑色总数
        for j in range(height):
            if thresh[j][i] == 255:
                line_white += 1
            if thresh[j][i] == 0:
                line_black += 1
        white_max = max(white_max, line_white)
        black_max = max(black_max, line_black)
        white.append(line_white)
        black.append(line_black)
        # print('white_max', white_max)
        # print('black_max', black_max)
    # arg为true表示黑底白字，False为白底黑字
    arg = True
    if black_max < white_max:
        arg = False

    # 分割车牌字符
    n = 1
    while n < width - 2:
        n += 1
        # 判断是白底黑字还是黑底白字  0.05参数对应上面的0.95 可作调整
        if (white[n] if arg else black[n]) > (0.05 * white_max if arg else 0.05 * black_max):  # 这点没有理解透彻
            start = n
            end = find_end(start, arg, black, white, width, black_max, white_max)
            n = end
            if end - start > 5 or end > (width * 3 / 7):
                cropImg = thresh[0:height, start-1:end+1]
                # 对分割出的数字、字母进行resize并保存
                cropImg = cv.resize(cropImg, (34, 56))
                cv.imwrite(save_path + '\\{}.bmp'.format(n), cropImg)


def main():
    # 读取图像
    image = cv.imread(img_path)
    # 图像预处理，返回img_resized和定位的车牌矩形区域
    rect, img_resized = preprocessing(image)
    # 裁剪出车牌
    license_img = cut_license(img_resized, rect)
    cv.imshow('License', license_img)
    # 去除车牌上下无用边缘
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    for i in range(0,49):
        # Step1  读入灰度图
        img_path = r'D:/acode/Python/GetLisence/img/mi52020/IMG_ (%d).jpg'%(i+1)  # (600, 800, 3)  行，列，通道数
        save_path = 'img'
        main()
