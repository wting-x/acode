import cv2 as cv
import numpy as np

Min_Area = 2000


def DisplayImg(img):
    cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
    cv.imshow('input_image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 对minAreaRect获得的最小外接矩形，用纵横比进行判断
def verifySizes(RotatedRect):
    aspect = 4.7272
    min = 15 * aspect * 15
    max = 125 * aspect * 125
    height, width = RotatedRect[1]
    if height == 0 or width == 0:
        return False
    area = height * width
    r = width / height
    if r < 1:
        r = height / width
    if (area < 5000 or area > 2000) or (r < 5 or r > 2):
        return False
    else:
        return True

# 定位
def fixPosition(img_bin):
    # 检测所有外轮廓，只留矩形的四个顶点
    contours, _ = cv.findContours(img_bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # 形状及大小筛选校验
    det_x_max = 0
    det_y_max = 0
    num = 0

    for i in range(len(contours)):
        x_min = np.min(contours[i][:, :, 0])
        x_max = np.max(contours[i][:, :, 0])
        y_min = np.min(contours[i][:, :, 1])
        y_max = np.max(contours[i][:, :, 1])
        det_x = x_max - x_min
        det_y = y_max - y_min
        if det_y!=0 and (det_x / det_y > 1.8) and (det_x > det_x_max) and (det_y > det_y_max):
            det_y_max = det_y
            det_x_max = det_x
            num = i
    # 获取最可疑区域轮廓点集
    points = np.array(contours[num][:, 0])
    return points

def findVertices(points):
    # 获取最小外接矩阵，中心点坐标，宽高，旋转角度
    rect = cv.minAreaRect(points)
    # 获取矩形四个顶点，浮点型
    box = cv.boxPoints(rect)
    # 取整
    box = np.int0(box)
    # 获取四个顶点坐标

    left_point_x = np.min(box[:, 0])
    right_point_x = np.max(box[:, 0])
    top_point_y = np.min(box[:, 1])
    bottom_point_y = np.max(box[:, 1])

    left_point_y = box[:, 1][np.where(box[:, 0] == left_point_x)][0]
    right_point_y = box[:, 1][np.where(box[:, 0] == right_point_x)][0]
    top_point_x = box[:, 0][np.where(box[:, 1] == top_point_y)][0]
    bottom_point_x = box[:, 0][np.where(box[:, 1] == bottom_point_y)][0]
    # 上下左右四个点坐标
    vertices = np.array([[top_point_x, top_point_y], [bottom_point_x, bottom_point_y], [left_point_x, left_point_y], [right_point_x, right_point_y]])

    #左下右上四个顶点
    #vertices = np.array([[left_point_x, top_point_y], [left_point_x, bottom_point_y], [right_point_x, bottom_point_y], [right_point_x,top_point_y]])
    return vertices, rect
def Myright_point_y(vertices):
    a=vertices[0,0]-vertices[1,0]
    b=vertices[1,0]-vertices[3,0]
    i=a*vertices[3,1]+b*vertices[0,1]
    j=vertices[0,0]-vertices[3,0]
    i=i/j
    return i
def tiltCorrection(vertices, rect):
    #基本水平
    #if
    # 畸变情况1
    #if rect[2] > -45 and rect<-10:
    if rect[2] > -45:
        new_right_point_x = vertices[0, 0]
        new_right_point_y = int(vertices[1, 1] - (vertices[0, 0]- vertices[1, 0]) / (vertices[3, 0] - vertices[1, 0]) * (vertices[1, 1] - vertices[3, 1]))

        new_left_point_x = vertices[1, 0]
        new_left_point_y = int(vertices[0, 1] + (vertices[0, 0] - vertices[1, 0]) / (vertices[0, 0] - vertices[2, 0]) * (vertices[2, 1] - vertices[0, 1]))
        # 校正后的四个顶点坐标
        point_set_1 = np.float32([[440, 0],[0, 0],[0, 140],[440, 140]])
    # 畸变情况2
    elif rect[2] < -45:
        new_right_point_x = vertices[1, 0]
        new_right_point_y = int(vertices[0, 1] + (vertices[1, 0] - vertices[0, 0]) / (vertices[3, 0] - vertices[0, 0]) * (vertices[3, 1] - vertices[0, 1]))
        #y=Myright_point_y(vertices)
        new_left_point_x = vertices[0, 0]
        new_left_point_y = int(vertices[1, 1] - (vertices[1, 0] - vertices[0, 0]) / (vertices[1, 0] - vertices[2, 0]) * (vertices[1, 1] - vertices[2, 1]))
        # 校正后的四个顶点坐标
        point_set_1 = np.float32([[0, 0],[0, 140],[440, 140],[440, 0]])

    # 校正前平行四边形四个顶点坐标
    new_box = np.array([(vertices[0, 0], vertices[0, 1]), (new_left_point_x, new_left_point_y), (vertices[1, 0], vertices[1, 1]), (new_right_point_x, new_right_point_y)])
    point_set_0 = np.float32(new_box)
    return point_set_0, point_set_1, new_box
def transform(img, point_set_0, point_set_1):
    # 变换矩阵
    mat = cv.getPerspectiveTransform(point_set_0, point_set_1)
    # 投影变换
    lic = cv.warpPerspective(img, mat, (440, 140))
    return lic

def get4Point(vertices):
    minx=np.min(vertices[:, 0])
    maxx=np.max(vertices[:, 0])
    miny=np.min(vertices[:, 1])
    maxy=np.max(vertices[:, 1])
    print('minx=',minx,'maxx=',maxx)
    return np.array([[maxx,miny],[maxx,maxy],[minx,maxy],[minx,miny]])

for i in range(0,49):
    # Step1  读入灰度图
    initial_car = cv.imread(r'D:/acode/Python/GetLisence/img/mi52020/IMG_ (%d).jpg'%(i+1))  # (600, 800, 3)  行，列，通道数
    #initial_car = cv.imread(r'U6T73.jpg')  # (600, 800, 3)  行，列，通道数
    # 统一规定大小
    if initial_car.shape[0]<=initial_car.shape[1]:
        initial_car = cv.resize(initial_car,(640,480),)
    else:
        initial_car = cv.resize(initial_car,(480,640),)

    gray_car = cv.cvtColor(initial_car, cv.COLOR_BGR2GRAY)
    # Step2  高斯模糊处理
    blur_car = cv.GaussianBlur(gray_car, (7,7), 0)
    # Step3  Sobel计算水平导数
    sobel_car = cv.Sobel(blur_car, cv.CV_16S, 1, 0)
    sobel_car = cv.convertScaleAbs(sobel_car)  # 转回uint8
    # Step4  Otsu大津算法自适应阈值二值化
    _, otsu_car = cv.threshold(sobel_car, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
    # DisplayImg(otsu_car)
    # Step5  闭操作
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (7,7))
    close_car = cv.morphologyEx(otsu_car, cv.MORPH_CLOSE, kernel)

    #DisplayImg(close_car)
    points=fixPosition(close_car)
    vertices, rect = findVertices(points)
    if rect[2]<-10:
        point_set_0, point_set_1, new_box = tiltCorrection(vertices, rect)
        img_draw = cv.drawContours(initial_car.copy(), [new_box], -1, (0,0,255), 3)
        lic = transform(initial_car, point_set_0, point_set_1)
    else:
        new_box=get4Point(vertices)
        img_draw = cv.drawContours(initial_car.copy(), [new_box], -1, (0,0,255), 3)
        minx=np.min(new_box[:,0])
        maxx=np.max(new_box[:,0])
        miny=np.min(new_box[:,1])
        maxy=np.max(new_box[:,1])
        #print('otsu_car=',otsu_car.shape)
        lic=initial_car[miny:maxy,minx:maxx]
        lic=cv.resize(lic,(440,140))
    cv.imshow("Frame",img_draw)
    # 暂停、关闭窗口
    cv.waitKey(0)
    cv.destroyAllWindows()
