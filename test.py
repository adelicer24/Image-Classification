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
output = ((label[0][0]+label[0][1]+label[0][2]+label[0][3]+label[0][4]+label[0][5]+label[0][6]+label[0][7]+label[0][8]+label[0][9])/11)*1000
accuracy = round(output, 2)
accuracy = str(accuracy)

with open('output.txt', 'w') as f:
    f.write(accuracy)