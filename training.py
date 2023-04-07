from keras.utils import np_utils
from keras.datasets import cifar10

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense

from tensorflow.keras.optimizers import Adam
from keras.callbacks import Callback

from keras import backend as K
import numpy as np

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

mean = np.mean(x_train,axis=(0,1,2,3))
std = np.std(x_train,axis=(0,1,2,3))
x_train = (x_train-mean)/(std+1e-7)
x_test = (x_test-mean)/(std+1e-7)

nClasses = 10
y_train = np_utils.to_categorical(y_train,nClasses)
y_test = np_utils.to_categorical(y_test,nClasses)

input_shape = (32,32,3)

def createModel():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=input_shape))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nClasses, activation='softmax'))

    return model

K.clear_session()
model = createModel()

AdamOpt = Adam(lr=0.001)
model.compile(optimizer='Adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])

batch_size = 256
epochs = 50

class CustomCallback(Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (epoch % 5 == 0):
            print("Finished epoch", epoch)
            print("-----------------------------------")
            print('Loss evaluated on the validation dataset =', 
                  logs.get('val_loss'))
            print('Accuracy reached train is', 
                  logs.get('acc'))
            print('Accuracy reached Val is', 
                  logs.get('val_acc'))
            return

CC = CustomCallback()
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
                    verbose=0,
                    validation_data=(x_test, y_test),
                    callbacks = [CC])

model.save('model_saved.h5')