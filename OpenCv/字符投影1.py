import cv2
import numpy
img = cv2.imread('/Users/apple/PycharmProjects/keras/image/data/preview/0000a_0.png_0_7473.png', cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]
#resized = cv2.resize(img, (3*width,3*height), interpolation=cv2.INTER_CUBIC)
#二值化
(_, thresh) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
#cv2.imshow('thresh', thresh)
#扩大黑色面积，使效果更明显
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))#形态学处理，定义矩形结构
closed = cv2.erode(thresh, None, iterations = 5)
cv2.imshow('erode',closed)
height, width = closed.shape[:2]
v = [0]*width
z = [0]*height
a = 0
#垂直投影
#统计并存储每一列的黑点数
for x in range(0, width):
    for y in range(0, height):
        if closed[y,x][0] == 0:
            a = a + 1
        else :
            continue
    v[x] = a
    a = 0
l = len(v)
#print l
#print width
#创建空白图片，绘制垂直投影图
emptyImage = numpy.zeros((height, width, 3), numpy.uint8)
for x in range(0,width):
    for y in range(0, v[x]):
        b = (255,255,255)
        emptyImage[y,x] = b
cv2.imshow('chuizhi', emptyImage)
#水平投影
#统计每一行的黑点数
a = 0
emptyImage1 = numpy.zeros((height, width, 3), numpy.uint8)
for y in range(0, height):
    for x in range(0, width):
        if closed[y,x][0] == 0:
            a = a + 1
        else :
            continue
    z[y] = a
    a = 0
l = len(z)
#print l
#print height
#绘制水平投影图
for y in range(0,height):
    for x in range(0, z[y]):
        b = (255,255,255)
        emptyImage1[y,x] = b
cv2.imshow('shuipin', emptyImage1)
cv2.waitKey(0)

