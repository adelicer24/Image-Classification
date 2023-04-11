from keras.models import load_model
from tensorflow.keras.utils import load_img
import numpy as np
 
from keras.models import load_model
 
model = load_model('model_saved.h5')

images = ['static/css/images/airplane1.jpg',
          'static/css/images/airplane2.jpg',
          'static/css/images/airplane3.jpg',
          'static/css/images/airplane4.jpg',
          'static/css/images/bird1.jpg',
          'static/css/images/bird2.jpg',
          'static/css/images/bird3.jpg',
          'static/css/images/bird4.jpg',
          'static/css/images/car1.jpg',
          'static/css/images/car2.jpg',
          'static/css/images/car3.jpg',
          'static/css/images/car4.jpg',
          'static/css/images/cat1.jpg',
          'static/css/images/cat2.jpg',
          'static/css/images/cat3.jpg',
          'static/css/images/cat4.jpg',
          'static/css/images/deer1.jpg',
          'static/css/images/deer2.jpg',
          'static/css/images/deer3.jpg',
          'static/css/images/deer4.jpg',
          'static/css/images/dog1.jpg',
          'static/css/images/dog2.jpg',
          'static/css/images/dog3.jpg',
          'static/css/images/dog4.jpg',
          'static/css/images/frog1.jpg',
          'static/css/images/frog2.jpg',
          'static/css/images/frog3.jpg',
          'static/css/images/frog4.jpg',
          'static/css/images/horse1.jpg',
          'static/css/images/horse2.jpg',
          'static/css/images/horse3.jpg',
          'static/css/images/horse4.jpg',
          'static/css/images/ship1.jpg',
          'static/css/images/ship2.jpg',
          'static/css/images/ship3.jpg',
          'static/css/images/ship4.jpg',
          'static/css/images/truck1.jpg',
          'static/css/images/truck2.jpg',
          'static/css/images/truck3.jpg',
          'static/css/images/truck4.jpg']

image_picked = images[33]

image = load_img(image_picked, target_size=(32, 32))
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

print(image_picked)
print(output)
print(prediction)