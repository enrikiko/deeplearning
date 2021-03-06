from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
import numpy as np
import os
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

# Set IA
STEPS = 5 #8000
EPOCHS = 2  #25
VALIDATION_STEPS = 2 #2000

app = Flask(__name__)

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))

# Compiling the CNN
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Part 2 - Fitting the CNN to the images

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('training_set',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('test_set',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch=STEPS,
                         epochs=EPOCHS,
                         validation_data=test_set,
                         validation_steps=VALIDATION_STEPS)

# Part 3 - Making new predictions

# def catordog(imageName):
#     test_image = image.load_img(imageName, target_size=(64, 64))
#     test_image = image.img_to_array(test_image)
#     test_image = np.expand_dims(test_image, axis=0)
#     result = classifier.predict(test_image)
#     # training_set.class_indices
#     if result[0][0] == 1:
#         prediction = 'dog'
#     elif result[0][0] == 0:
#         prediction = 'cat'
#     else:
#         prediction = repr(result[0][0])
#     return prediction


#print(catordog("single_prediction/cat_or_dog_1.jpg"))
#print(catordog("single_prediction/cat_or_dog_2.jpg"))

# print("line 89")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    f = request.files['file']
    print("Filename:" + f.filename)
    f.save(secure_filename(f.filename))
    #return catordog(f.filename)
    test_image = image.load_img(f.filename, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)
    # training_set.class_indices
    if result[0][0] == 1:
        prediction = 'dog'
    elif result[0][0] == 0:
        prediction = 'cat'
    else:
        prediction = repr(result[0][0])
    return prediction
    # return 'file uploaded successfullyd'


@app.route('/liveness', methods=['GET'])
def liveness():
    return "I am alive"


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory('/src', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
def http():
    return '''
    <html>
       <body>
          <form action = upload method = "POST"
             enctype = "multipart/form-data">
             <input type = "file" name = "file" />
             <input type = "submit"/>
          </form>
       </body>
    </html>
    '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
