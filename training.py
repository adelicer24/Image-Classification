# The cifar10 image dataset being used to train the model is from
# https://www.cs.toronto.edu/~kriz/cifar.html

# This code below used to create, train, and save the model is from
# https://www.geeksforgeeks.org/python-image-classification-using-keras/
# https://youtu.be/VQYMOJnN6xg
# https://www.analyticsvidhya.com/blog/2020/10/create-image-classification-model-python-keras/

# This python file creates and trains the image classification model
# on images contained within the cifar10 dataset and saved the model

# This imports the cifar10 dataset to train my model
from keras.datasets import cifar10

# These are the imports necessary to create and train my model
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np
from tensorflow.keras.optimizers import Adam
from keras.callbacks import Callback

# This loads the data from the cifar10 dataset so it can be used to
# train the model 
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# This normalizes the data from the cifar10 dataset
mean = np.mean(x_train,axis=(0,1,2,3))
std = np.std(x_train,axis=(0,1,2,3))
x_train = (x_train-mean)/(std+1e-7)
x_test = (x_test-mean)/(std+1e-7)

# This defines the number of classes that are in the cifar10 dataset
nClasses = 10
y_train = np_utils.to_categorical(y_train,nClasses)
y_test = np_utils.to_categorical(y_test,nClasses)

# This defines the dimension of the images with the number of channels
# so the model will know what images it will be recieiving
input_shape = (32,32,3)

# This function creates the image classification model and returns it
# as an object
# Sequential allows multiple layers to be added onto the model
# Each call to Conv2D adds a 2D convolution over the input images
# MaxPooling2D reduces the dimensionality of the input images down
# to 2,2
# Flatten creates a copy of the image collapsed into one dimension
# Dense is used to make the model fully connected
# Dropout is used to avoid overfitting on the dataset
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

# This will remove everything from memory to train the model fresh
K.clear_session()

# This creates the model and stores it in a variable
model = createModel()

# This defines the optimizer to be used for the model
AdamOpt = Adam(lr=0.001)

# This compiles the model
model.compile(optimizer='Adam', loss='categorical_crossentropy', 
              metrics=['accuracy'])

# This defines the number of samples to be propagated through the model
batch_size = 256

# This defines the amount of cycles to train the model using the entire
# training dataset 
epochs = 50

# This function allows us to see the model's progress as it is being
# trained
# It will show us the loss evaluated, the training set accuracy, and
# validation set accuracy 
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

# This instantiates the CustomCallback class
CC = CustomCallback()

# This function adjusts the parameters in the model to help improve
# its accuracy
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs,
                    verbose=0,
                    validation_data=(x_test, y_test),
                    callbacks = [CC])

# This saves the model so it can be used for testing
model.save('model_saved.h5')