import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/apple/PycharmProjects/keras/OpenCv/1.jpeg',0)
dstimg = cv2.blur(img,ksize=(7,7))
cv2.imshow('均值滤波模糊', dstimg)
cv2.waitKey(0)
cv2.destroyAllWindows()