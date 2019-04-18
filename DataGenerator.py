from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
import SplitImg
import numpy as np

outpath = "/Users/apple/PycharmProjects/keras/image/preview"
inputpath = "/Users/apple/PycharmProjects/keras/image/splited"
wildcard = ".jpg .png"  # 要读取的文件类型；
path = []



def Generate():
   
    datagen = ImageDataGenerator (
        rotation_range=5,
        zoom_range=0.2,
        shear_range=5,
        fill_mode='nearest')
    
    for p in path:
       
        
        image = load_img (p)
        x = img_to_array (image)  # this is a Numpy array with shape (3, 150, 150)
        x = x.reshape ((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
        i = 0
        p = p [ 49:50 ]
        
        for batch in datagen.flow (x, batch_size=1, save_prefix=str (p), save_to_dir=outpath, save_format='png'):
          
            i += 1
            if i > 0:
                break  # otherwise the generator would loop indefinitely


def ListFilesToTxt (dir,  wildcard, recursion):
    
    exts = wildcard.split (" ")
    #过滤'.DS_Store'文件
    files = [ f for f in os.listdir (dir) if not f.startswith ('.') ]
    for name in files:
        fullname = os.path.join (dir, name)
        if (os.path.isdir (fullname) & recursion):
            ListFilesToTxt (fullname,  wildcard, recursion)
        else:
            for ext in exts:
                path.insert (path.__len__ (), fullname)
           

def GetPath ():
 
  
    ListFilesToTxt (inputpath,  wildcard, 1)
   



def DataGenerate():
    
    GetPath ()
    
    Generate ()





