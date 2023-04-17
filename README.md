# Image Classification Project

## Alex Delicer

### About

This website application will allow visitors to upload a digital image
of an object that the image classification algorithm can identify. The
website application will open with a welcome page that gives the users
a description of the website and its purpose. The user will then be able
to upload a digital image of the objects specified by the website. When
the image is uploaded, it will be passed to the algorithm to be identified.
After the image has been identified through by the algorithm, the image
will be displayed on the website along with the amount of time it took the
algorithm to identify the object and the algorithm's accuracy (if possible).
From there the user can submit another image if they would like to test the
algorithm again.

### Files

app.py - This file contains all of the web application routes

dict.py - This file contains all of the model's output and is run when
a user is using the web application to prevent the web application from
loading too long when 'testing' the model

test.py - This file contains the code to test the model on the test
images after it has been trained

training.py - This file contains the code to create and train the model
as well as save the model for testing

requirements.txt - Contains all the dependencies needed to allow the
project to work

### Installation

To install the dependencies necessary, use the command:
'pip install -r requirements.txt'

### How to use

Be sure to have already run the command 'pip install -r requirements.txt'
so that the necessary dependencies can be used. To train the model,
run the command 'python3 training.py'. This will create, train, and save
the model so that it can be tested. In the 'test.py' file, the user can
edit the 'image_picked' variable by changing the index of 'images' from
0 to 39 to test one of the forty test images. When an image is selected,
the command 'python3 test.py' can be run to test the model on the seleceted
image. 
To use the web application, run the command 'flask run' and then
ctrl + click on the link 'http://127.0.0.1:500' that appears to be
redirected to the web application. From there, the user can click on
the 'Classify an Image!' button to test the model. The user can then
select one of forty images to test the model on. After an image is
selected, the user can click the 'Classify!' button to be redirected
to the Results page to view the model's prediction. The user can then
click the 'Classify Another Image!' button to test the model again.