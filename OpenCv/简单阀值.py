import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('/Users/apple/PycharmProjects/keras/OpenCv/gery.jpg',0)

ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

title = ['Original Image', 'BINARY', 'BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
imgs = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

while (1):
	cv2.imshow (title [ 0 ], imgs [ 0 ])
	cv2.imshow (title [ 1 ], imgs [ 1 ])
	cv2.imshow (title [ 2 ], imgs [ 2 ])
	cv2.imshow (title [ 3 ], imgs [ 3 ])
	cv2.imshow (title [ 4 ], imgs [ 4 ])
	cv2.imshow (title [ 5 ], imgs [ 5 ])

	
	if cv2.waitKey (1) & 0xFF == 27:
		break
	

cv2.destroyAllWindows ()
