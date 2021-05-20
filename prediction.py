import cv2
import numpy as np
import os

from keras.preprocessing.image import load_img, img_to_array

os.environ['KMP_DUPLICATE_LIB_OK']='True'
from keras.models import load_model


model = load_model('model.h5')
img_path = '/Volumes/Transcend/媒体/code/vscode/keras-master/image/splited/5457.png'

img = cv2.imread(img_path)
img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
img = img_to_array(img)
img = np.expand_dims(img, axis=0)



out = model.predict(img)

list = list(out[0])
result = list.index(1)

print(result)

str = str(result)
img = cv2.imread(img_path,1)
cv2.imshow (str, img)
cv2.waitKey(0)
