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

def quadratic_transform_for_dim_2(feature):
    return [ [1, f[0], f[1], f[0]*f[1], f[0]**2, f[1]**2 ] for f in feature ]

def run_quadratic_regression(features, tags):
    transformed_features = quadratic_transform_for_dim_2(features)
    w_qua = run_linear_regression(transformed_features, tags)
    return w_qua, transformed_features

def generate_data_and_run_regression(data_size, flipping_prob):
    x, y = generate_data(data_size,flipping_prob)
    w_qua, transformed_z = run_quadratic_regression(x,y)
    err = 0
    for n in range(len(y)):
        if util.same_sign(np.dot(w_qua, transformed_z[n]), y[n]) == False:
            err += 1
    Ein = float(err) / len(y)
    return w_qua, Ein
