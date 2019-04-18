import os
import numpy as np



def ListFilesToTxt (dir, file, wildcard, recursion):
	exts = wildcard.split (" ")
	files = os.listdir (dir)
	for name in files:
		fullname = os.path.join (dir, name)
		if (os.path.isdir (fullname) & recursion):
			ListFilesToTxt (fullname, file, wildcard, recursion)
		else:
			for ext in exts:
				if (name.endswith (ext)):
					
					for i in name[:4]:
						
						file.write(i + '\n')
					
					break


def Test ():
	dir = "/Users/apple/PycharmProjects/keras/image/data/images"  # 文件路径
	outfile = "/Users/apple/Desktop/未命名文件夹/binaries.txt"  # 写入的txt文件名
	wildcard = ".jpg .png"  # 要读取的文件类型；
	
	file = open (outfile, "w")
	if not file:
		print ("cannot open the file %s for writing" % outfile)
	
	ListFilesToTxt (dir, file, wildcard, 1)
	
	file.close ()


Test ()
