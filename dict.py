# This python file contains the information that is displayed to the
# user on the web app side of my software

# This dictionary stores the image oaths and their predicted values
# given by my model
prediction_values = {'static/css/images/airplane1.jpg': 0.9999990463256836,
                     'static/css/images/airplane2.jpg': 0.9985594153404236,
                     'static/css/images/airplane3.jpg': 0.994929850101471,
                     'static/css/images/airplane4.jpg': 0.9064414501190186,
                     'static/css/images/bird1.jpg': 0.0010113585740327835,
                     'static/css/images/bird2.jpg': 0.002240208676084876,
                     'static/css/images/bird3.jpg': 0.0013502476504072547,
                     'static/css/images/bird4.jpg': 0.0019581217784434557,
                     'static/css/images/car1.jpg': 3.678183566080406e-05,
                     'static/css/images/car2.jpg': 5.800125654786825e-05,
                     'static/css/images/car3.jpg': 1.1575825737963896e-05,
                     'static/css/images/car4.jpg': 4.474594970815815e-05,
                     'static/css/images/cat1.jpg': 8.799844181339722e-06,
                     'static/css/images/cat2.jpg': 6.7823916651832405e-06,
                     'static/css/images/cat3.jpg': 5.754071480623679e-06,
                     'static/css/images/cat4.jpg': 6.776565442123683e-06,
                     'static/css/images/deer1.jpg': 3.744234180921803e-15,
                     'static/css/images/deer2.jpg': 1.0177138977743045e-15,
                     'static/css/images/deer3.jpg': 1.7654423963584052e-15,
                     'static/css/images/deer4.jpg': 1.1155380504900589e-15,
                     'static/css/images/dog1.jpg': 1.186959142085442e-10,
                     'static/css/images/dog2.jpg': 5.670454661377278e-10,
                     'static/css/images/dog3.jpg': 3.3816217187565556e-11,
                     'static/css/images/dog4.jpg': 5.175063155782311e-10,
                     'static/css/images/frog1.jpg': 5.809031641129669e-13,
                     'static/css/images/frog2.jpg': 8.719749748642425e-12,
                     'static/css/images/frog3.jpg': 8.256352199143002e-12,
                     'static/css/images/frog4.jpg': 8.716941421070198e-14,
                     'static/css/images/horse1.jpg': 2.5601559627830284e-07,
                     'static/css/images/horse2.jpg': 1.960157987923594e-06,
                     'static/css/images/horse3.jpg': 1.873564087873092e-06,
                     'static/css/images/horse4.jpg': 1.9279514162917621e-07,
                     'static/css/images/ship1.jpg': 4.1926688787441435e-09,
                     'static/css/images/ship2.jpg': 6.051895873326885e-09,
                     'static/css/images/ship3.jpg': 3.569959616811502e-08,
                     'static/css/images/ship4.jpg': 5.523628665571323e-09,
                     'static/css/images/truck1.jpg': 0.12237711995840073,
                     'static/css/images/truck2.jpg': 0.02286165952682495,
                     'static/css/images/truck3.jpg': 0.47711536288261414,
                     'static/css/images/truck4.jpg': 0.015482001937925816}

# This dictionary stores the image paths and the model's runtime when
# predicting them
prediction_runtime = {'static/css/images/airplane1.jpg': '0s 417ms/step',
                     'static/css/images/airplane2.jpg': '0s 293ms/step',
                     'static/css/images/airplane3.jpg': '0s 466ms/step',
                     'static/css/images/airplane4.jpg': '0s 265ms/step',
                     'static/css/images/bird1.jpg': '0s 348ms/step',
                     'static/css/images/bird2.jpg': '0s 276ms/step',
                     'static/css/images/bird3.jpg': '0s 263ms/step',
                     'static/css/images/bird4.jpg': '0s 259ms/step',
                     'static/css/images/car1.jpg': '0s 265ms/step',
                     'static/css/images/car2.jpg': '0s 267ms/step',
                     'static/css/images/car3.jpg': '1s 560ms/step',
                     'static/css/images/car4.jpg': '0s 279ms/step',
                     'static/css/images/cat1.jpg': '0s 312ms/step',
                     'static/css/images/cat2.jpg': '0s 372ms/step',
                     'static/css/images/cat3.jpg': '0s 264ms/step',
                     'static/css/images/cat4.jpg': '0s 258ms/step',
                     'static/css/images/deer1.jpg': '0s 272ms/step',
                     'static/css/images/deer2.jpg': '1s 614ms/step',
                     'static/css/images/deer3.jpg': '0s 280ms/step',
                     'static/css/images/deer4.jpg': '0s 268ms/step',
                     'static/css/images/dog1.jpg': '0s 269ms/step',
                     'static/css/images/dog2.jpg': '0s 275ms/step',
                     'static/css/images/dog3.jpg': '0s 259ms/step',
                     'static/css/images/dog4.jpg': '0s 367ms/step',
                     'static/css/images/frog1.jpg': '0s 279ms/step',
                     'static/css/images/frog2.jpg': '0s 264ms/step',
                     'static/css/images/frog3.jpg': '0s 260ms/step',
                     'static/css/images/frog4.jpg': '0s 255ms/step',
                     'static/css/images/horse1.jpg': '0s 265ms/step',
                     'static/css/images/horse2.jpg': '0s 362ms/step',
                     'static/css/images/horse3.jpg': '0s 261ms/step',
                     'static/css/images/horse4.jpg': '0s 306ms/step',
                     'static/css/images/ship1.jpg': '0s 258ms/step',
                     'static/css/images/ship2.jpg': '0s 353ms/step',
                     'static/css/images/ship3.jpg': '0s 251ms/step',
                     'static/css/images/ship4.jpg': '0s 390ms/step',
                     'static/css/images/truck1.jpg': '0s 316ms/step',
                     'static/css/images/truck2.jpg': '0s 285ms/step',
                     'static/css/images/truck3.jpg': '0s 356ms/step',
                     'static/css/images/truck4.jpg': '0s 244ms/step'}

# This retrieves the path of the image chosen by the user
with open('image.txt', 'r') as image:
    url = image.read()

# Output stores the predicted value given by the model for the image
# chosen by the user 
output = prediction_values[url]

# Runtime stores the runtime of the model when predicting the image
# chosen by the user
runtime = prediction_runtime[url]

# This variable will hold the name of the class that the image is
# predicted to be in
prediction = "None"

# The if statements below takes the model's predicted value and
# categorizes it into which ever class it falls into
def predictTranslator(output):
    if (output> 0.9 and output< 1.0):
        prediction = "Airplane"
    if (output> 0.0010 and output< 0.0025):
        prediction = "Bird"
    if (output> 1.0e-05 and output< 6.0e-05):
        prediction = "Car"
    if (output> 5.0e-6 and output< 9.0e-6):
        prediction = "Cat"
    if (output> 3.0e-11 and output< 6.0e-10):
        prediction = "Dog"
    if (output> 1.0e-15 and output< 4.0e-15):
        prediction = "Deer"
    if (output> 8.0e-14 and output< 9.0e-12):
        prediction = "Frog"
    if (output> 1.5e-07 and output< 2.0e-06):
        prediction = "Horse"
    if (output> 1.0e-09 and output< 9.0e-08):
        prediction = "Ship"
    if (output> 0.01 and output< 0.5):
        prediction = "Truck"
    return prediction

# This writes the model's prediction in a txt file
with open('prediction.txt', 'w') as f:
    f.write(predictTranslator(output))

# This writes the model's runtime in a txt file
with open('runtime.txt', 'w') as f:
    f.write(runtime)