
import numpy as  np
import cv2

img = cv2.imread('/Users/apple/PycharmProjects/keras/image/data/test_images/6.jpeg')
rows,cols,ch = img.shape

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

while(1):
	cv2.imshow ('Input', img)
	cv2.imshow ('Output', dst)
	if cv2.waitKey(1) & 0xFF == 27:
		break


cv2.destroyAllWindows()
