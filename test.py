from keras.models import load_model
from tensorflow.keras.utils import load_img
import numpy as np
 
from keras.models import load_model
 
model = load_model('model_saved.h5')

with open('image.txt', 'r') as image:
    url = image.read()

image = load_img(url, target_size=(32, 32))
img = np.array(image)
img = img / 255.0
img = img.reshape(1,32,32,3)
label = model.predict(img)

output = float(label[0][0])
prediction = "None"

if (output > 0.9 and output < 1.0):
    prediction = "Airplane"
if (output > 0.0010 and output < 0.0025):
    prediction = "Bird"
if (output > 1.0e-05 and output < 6.0e-05):
    prediction = "Car"
if (output > 5.0e-6 and output < 9.0e-6):
    prediction = "Cat"
if (output > 3.0e-11 and output < 6.0e-10):
    prediction = "Dog"
if (output > 1.0e-15 and output < 4.0e-15):
    prediction = "Deer"
if (output > 8.0e-14 and output < 9.0e-12):
    prediction = "Frog"
if (output > 1.5e-07 and output < 2.0e-06):
    prediction = "Horse"
if (output > 1.0e-09 and output < 9.0e-08):
    prediction = "Ship"
if (output > 0.01 and output < 0.5):
    prediction = "Truck"

with open('prediction.txt', 'w') as f:
    f.write(prediction)