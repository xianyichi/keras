
import numpy as  np
import cv2

img = cv2.imread('/Users/apple/PycharmProjects/keras/OpenCv/sword.jpg')
rows,cols = img.shape[:2]
#这里的第一个参数为旋转中心，第二个为选装角度，第三个为旋转后的缩放因子
#可以通过谁在旋转中心，缩放因子，以及窗口大小来放置旋转后超出边界的问题

M = cv2.getRotationMatrix2D((cols/2, rows/2),45,0.6)

#第三个参数的你输出图像的尺寸中心
dst = cv2.warpAffine(img,M,(2*cols, 2*rows))
cv2.imshow('img',dst)
cv2.waitKey(6000)
cv2.destroyAllWindows()