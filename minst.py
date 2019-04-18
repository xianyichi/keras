from keras.datasets import mnist
from keras import models, layers
from keras.utils import to_categorical
import ImportData
import matplotlib.pyplot as plt

train_images, train_labels,test_images, test_labels = ImportData.importData()
print(train_images.shape,train_labels.shape,test_images.shape,test_labels.shape)

# network = models.Sequential()
# network.add(layers.Dense(512, activation='relu', input_shape=(46 * 30,)))
# network.add(layers.Dense(11, activation='softmax'))
#
# network.compile(optimizer='rmsprop',
#                 loss='categorical_crossentropy',
#                 metrics=['accuracy'])

# network.fit(train_images, train_labels, epochs=5, batch_size=128)
#test_loss, test_acc = network.evaluate(test_images, test_labels)
#

train_images = train_images.astype('float32')/255
test_images = test_images.astype('float32')/255
#onehotch处理
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(46,30,1)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(11,activation='softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])



# model.fit(train_images,train_labels,epochs=10,batch_size=128)
# test_loss, test_acc = model.evaluate(test_images,test_labels)
# print('test_acc:', test_acc)
#



history = model.fit(train_images,
                    train_labels,
                    epochs=10,
                    batch_size=128,
                    validation_data=(test_images, test_labels))

history_dic = history.history
loss_values = history_dic['loss']
val_loss_values = history_dic['val_loss']

epochs = range(1, len(loss_values) + 1)

plt.plot(epochs, loss_values, 'bo', label='Training loss')
plt.plot(epochs, val_loss_values, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()

plt.clf()
acc = history_dic['acc']
val_acc = history_dic['val_acc']

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validtion accuracy')
plt.xlabel('Epochs')
plt.ylabel(('Accuracy'))
plt.legend()

plt.show()
