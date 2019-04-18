'''onehot处理'''

import numpy as np
import tensorflow as tf



label = np.array ([ 2,2,6,11])  ##标签数据，标签从0开始
classes = max (label) + 1  ##类别数为最大数加1
one_hot_label = np.zeros (shape=(label.shape [ 0 ], classes))  ##生成全0矩阵
one_hot_label [ np.arange (0, label.shape [ 0 ]), label ] = 1  ##相应标签位置置1
print (one_hot_label)




# label = np.array ([ 0, 3, 2, 8, 9, 1 ,11])  ##标签数据，标签从0开始
# classes = max (label) + 1  ##类别数为最大数加1
# label_concatenated = np.concatenate ((np.arange (0, label.shape [ 0 ]).reshape (-1, 1), label.reshape (-1, 1)),
#                                      axis=1)  ####转成one_hot向量！！
# train_label = tf.sparse_to_dense (label_concatenated, [ label.shape [ 0 ], classes ], 1, 0)
#
# with tf.Session () as sess:
# 	print(sess.run(train_label))
