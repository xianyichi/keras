import os,numpy as np
from keras.preprocessing.image import load_img, img_to_array
import cv2,random
import DataGenerator,SplitImg

train_dir = '/Users/apple/PycharmProjects/keras/image/preview'
labelfile = "/Users/apple/PycharmProjects/keras/image/label.txt"
img_list = [ ]
data_list = [ ]
wildcard = ".jpg .png"



def ImportImage (dir, wildcard, ):

	
	#labeltext = open(labelfile,"w")
	exts = wildcard.split (" ")
	# 过滤'.DS_Store'文件
	files = files = [ f for f in os.listdir (dir) if not f.startswith ('.') ]
	random.shuffle(files)
	for i in files:
		if i[0] == '_':
			p = '10'
		else:
			p = i[0]
		data_list.append(p)
		
	print(files.__len__())
	for name in files:
		
		fullname = os.path.join (dir, name)
		if (os.path.isdir (fullname)):
			ImportImage (fullname, wildcard)
		else:
			for ext in exts:
				if (name.endswith (ext)):
					img = cv2.imread(fullname)
					oimg = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
					array = img_to_array (oimg)
					#labeltext.write (name [ 0 ] + '\n')
					img_list.append (array)
					break

	print(files.__len__())
	print(data_list)
	


def importData ():
	
	
	# SplitImg.Split()
	# DataGenerator.DataGenerate()
	
	ImportImage (train_dir, wildcard)

	#
	train_images = np.array (img_list)
	train_labels = np.array (data_list)
	
	i = int(train_images.__len__()/3)
	l = int(train_labels.__len__()/3)
	
	#准备训练数据
	test_images = train_images[:i]
	test_labels = train_labels[:l]
	#准备验证数据
	train_images = train_images[i:]
	train_labels = train_labels[l:]
	
	return train_images, train_labels,test_images,test_labels



