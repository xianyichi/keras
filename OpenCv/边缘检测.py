import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/Users/apple/PycharmProjects/keras/image/data/test_images/9.jpeg',0)
blur = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(blur,3,9,3)


# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()
#



cv2.imshow('Canny边缘检测',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()