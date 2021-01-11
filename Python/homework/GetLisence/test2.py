import cv2

# 使用的是HyperLPR已经训练好了的分类器
watch_cascade = cv2.CascadeClassifier('cascade.xml')

# 先读取图片

for i in range(0,49):
    image = cv2.imread(r'D:/acode/Python/GetLisence/img/mi52020/IMG_ (%d).jpg'%(i+1))     #输入自己的图片
    if image.shape[0]<=image.shape[1]:
            image = cv2.resize(image,(800,600),)
    else:
        image = cv2.resize(image,(600,800),)

    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    watches = watch_cascade.detectMultiScale(image_gray, 1.1, 2, minSize=(36, 9), maxSize=(36*40, 9*40))

    print('[INF0]:Detect %d license plates' % len(watches))
    for (x, y, w, h) in watches:
        if w*h >800 and w*h <5000:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()