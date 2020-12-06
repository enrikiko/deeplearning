from functions import save
from functions import sendHttp
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

startDate={ "Start" : time.time(),
    "Version" : "4init.py" }

#sendHttp(startDate)

# Importing the dataset
dataset = pd. read_csv('Churn_Modelling.csv')
x = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x_1 = LabelEncoder()
labelencoder_x_2 = LabelEncoder()

# Convert Srtring to Number
x[:, 1] = labelencoder_x_1.fit_transform(x[:, 1])
x[:, 2] = labelencoder_x_2.fit_transform(x[:, 2])

# Encode dumy parameters
onehotencoder = OneHotEncoder(categorical_features = [1], handle_unknown='ignore', dtype=np.integer)
x = onehotencoder.fit_transform(x).toarray()
x = x[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import  keras
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

def build_classifier(neuronN, neuronP):
    classifier = Sequential()
    classifier.add(Dense(units = neuronN, kernel_initializer = 'uniform', activation = 'relu', input_dim = 11))
    classifier.add(Dense(units = neuronP, kernel_initializer = 'uniform', activation = 'relu'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'rmsprop', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier

classifier = KerasClassifier(build_fn = build_classifier, batch_size = 10, epochs = 300)
parameters = {
'neuronN' : [6, 7],
'neuronP' : [6, 7]
}

#sendHttp(parameters)

grid_search = GridSearchCV(estimator = classifier,
param_grid = parameters,
scoring = 'accuracy',
cv = 10)
grid_search = grid_search.fit(x_train, y_train)
best_parameters = grid_search.best_params_
best_accuracy = grid_search.best_score_
print(best_parameters)
print(best_accuracy)
final={ "best_parameters" : best_parameters,
        "best_accuracy" : best_accuracy,
        "Finish" : time.time()       }
#sendHttp(final)
save(str(parameters))
save(str(best_parameters))
save(str(best_accuracy))
#accurancies = cross_val_score(estimator = classifier, X = x_train, y = y_train, cv = 10, n_jobs = -1 )
#mean = accurancies.mean()
#variance = accurancies.std()
