import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/apple/PycharmProjects/keras/OpenCv/1.jpeg',0)
edges = cv2.Canny(img,100,100)

element = cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(15,15))
eroded = cv2.erode(img,element)

cv2.imshow('123',eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()