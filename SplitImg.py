import cv2
import numpy as np
import os

#分割图片输出路径
path = '/Users/apple/PycharmProjects/keras/image/splited/'
#待分割图片路径
inputdir = "/Users/apple/PycharmProjects/keras/image/data/images"
# #label文件输出路径
# labelfile = "/Users/apple/PycharmProjects/keras/image/data/label.txt"
wildcard = ".jpg .png"  # 要读取的文件类型；

def SpliteImage(inputdir, wildcard, recursion):
	label = []
	exts = wildcard.split (" ")
	files = os.listdir (inputdir)
	for name in files:
		fullname = os.path.join (inputdir, name)
		if (os.path.isdir (fullname) & recursion):
			SpliteImage (fullname, wildcard, recursion)
		else:
			for ext in exts:
				if (name.endswith (ext)):
					#读取图片
					img = cv2.imread(fullname,)
					#获取图片像素数据
					rows,cols = img.shape[:2]
					#将图片四等分
					length = np.array([0,cols/4,cols/2,cols/(4/3),cols])
					l = 0
					for i in name [ :4 ]:
						simg = img[0:rows,int(length[l]):int(length[l+1])]
						# 图片输出路径+标签+图片格式
						imgoutpath = path + i + str (label.__len__ ()) + ext
						# 输出图片
						cv2.imwrite (imgoutpath, simg)
						label.insert (label.__len__ (), i + '\n')
						l += 1
					break

def Split():
	SpliteImage (inputdir, wildcard, 1)
	