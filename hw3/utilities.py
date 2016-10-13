import numpy as np
from pkg import utilities as util

LOWER_BOUND = -1
HIGHER_BOUND = 1
DIMENSION=2

def generate_data(data_size, flipping_prob, dimension=DIMENSION,
        low=LOWER_BOUND, high=HIGHER_BOUND):
    x = np.random.uniform(low=low,high=high,size=(data_size,dimension))
    y = [circular_target_function(i) * util.flip_sign_with_probability(flipping_prob) for i in x]
    return x,y

def circular_target_function(feature):
    result = 0
    for x_i in feature:
        result += x_i * x_i
    return util.sign(result-0.6)

def add_constant_term(feature):
    return [ [1]+f for f in feature ]

def run_linear_regression(feature, label):
    pseudo_inverse_x = np.linalg.pinv(feature)
    w_lin = np.dot(pseudo_inverse_x, label)
    return w_lin
