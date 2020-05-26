from keras.datasets import mnist
dataset = mnist.load_data("minst_data.db")
train, test = dataset
x_train, y_train = train
x_test, y_test = test
import cv2
img_label1= x_train[0]
print(img_label1.shape)
x_train = x_train.reshape(-1,28*28)
x_test = x_test.reshape(-1,28*28)
print(x_train.shape)
print(y_train.shape)
x_train=x_train.astype("float32")
x_test=x_test.astype("float32")
from keras.utils.np_utils import to_categorical
y_train = to_categorical(y_train)
print(y_train)
print(y_test)
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add(Dense(units=512, input_dim=28*28, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
print(model.summary())
from keras.optimizers import Adam
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
mod=model.fit(x_train, y_train, epochs=5)
print(x_test[0].shape)
m= model.predict(x_test)
print(y_test)
print(m[0])
print(m[1])
accuracy=mod.history['accuracy'][-1]