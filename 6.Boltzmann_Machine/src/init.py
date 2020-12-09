# Importin libraries
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
from torch.autograd import Variable

# Import the dataset
movies = pd.read_csv('movies.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')
users  = pd.read_csv('users.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')
ratings  = pd.read_csv('ratings.dat', sep = '::', header = None, engine = 'python', encoding = 'latin-1')

# Preparin the training set and the test set
training_set = pd.read_csv('u1.base', delimiter = '\t')
test_set = pd.read_csv('u1.test', delimiter = '\t')

training_set = np.array(training_set, dtype = 'int')
test_set = np.array(test_set, dtype = 'int')

# Getting the number of user and movies
nb_users = int(max(max(training_set[:,0]), max(test_set[:,0])))
nb_movies = int(max(max(training_set[:,1]), max(test_set[:,1])))

# Converting the data into an array with users in lines and movies in columns
def convert(data):
    new_data = []
    for id_users in range(1, nb_users + 1):
        id_movies = data[:,1][data[:,0] == id_users ]
        id_ratings = data[:,2][data[:,0] == id_users ]
        ratings = np.zeros(nb_movies)
        ratings[id_movies - 1] = id_ratings
        new_data.append(list(ratings))
    return new_data

training_set = convert(training_set)
test_set = convert(test_set)

# Coverting the data into Torch tensors
training_set = torch.FloatTensor(training_set)
test_set = torch.FloatTensor(test_set)

# Converting the ratings into binary ratings 1 (Likes) or 0 (Not Likes)
training_set[training_set == 0] = -1
training_set[training_set == 1] = 0
training_set[training_set == 2] = 0
training_set[training_set >= 3] = 1

test_set[test_set == 0] = -1
test_set[test_set == 1] = 0
test_set[test_set == 2] = 0
test_set[test_set >= 3] = 1

# Creating the architecture of the Neural Network
class RBM():
    def __init__(sefl, nv, nh):
        self.W = torch.randn(nh, nv)
        self.a = torch.randn(1, nh)
        self.b = torch.randn(1, nv)
    def sample_h(self, x):
        wx = torch.mm(x, self.W.t())
        activation = wx + self.a.expand_as(wx)
        p_h_given_v =  torch.sigmoid(activation)
        return p_h_given_v, torch.bernoulli(p_h_given_v)
    def sample_v(self, y):
        wy = torch.mm(y, self.W)
        activation = wy + self.b.expand_as(wy)
        p_h_given_h =  torch.sigmoid(activation)
        return p_h_given_h, torch.bernoulli(p_h_given_h)
    














# End
