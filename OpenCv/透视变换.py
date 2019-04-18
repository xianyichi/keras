import numpy as  np
import cv2

img = cv2.imread('/Users/apple/PycharmProjects/keras/image/data/test_images/6.jpeg')
rows,cols,ch = img.shape
pts1 = np.float32([[56,56],[368,52],[28,387],[389,389]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(rows,cols))

while(1):
	cv2.imshow('Input',img)
	cv2.imshow('Output',dst)
	
	if cv2.waitKey(1) & 0xFF == 27:
		break

cv2.destroyAllWindows()