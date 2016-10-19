import numpy as np
from pkg import utilities as util

LOWER_BOUND = -1
HIGHER_BOUND = 1
DIMENSION=2
UPDATE_TIMES = 2000

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

def train_by_gradient_descent(features, tags, gradient_func, eta=1, update_times=UPDATE_TIMES):
    weight_score = np.zeros(len(features[0]))
    for i in range(update_times):
        gradient = gradient_func(features, tags, weight_score)
        if gradient.all() == 0:
            break
        weight_score = np.add(weight_score, -eta*gradient)
    return weight_score


def test_data_from_hypothesis(features, tags, weight_score, error_measure_function):
    err = 0
    for n in range(len(tags)):
        if error_measure_function(features[n], tags[n], weight_score) == True:
            err += 1

    Err = float(err) / len(features)
    return Err

def one_zero_error(feature, tag, weight_score):
    return util.same_sign(np.dot(weight_score, feature), tag) == False


def batch_gradient_descent_theta(features, tags, weight_score):
    gradient_result = np.zeros(len(features[0]))
    for i in range(len(features)):
        gradient_result = np.add(gradient_result, -tags[i]*features[i]*theta_function(-tags[i]*np.dot(features[i], weight_score)))
    return np.divide(gradient_result, len(features))

def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called+= 1
        return fn(*args, **kwargs)
    wrapper.called= 0
    wrapper.__name__= fn.__name__
    return wrapper

@counted
def stochastic_gradient_descent_theta(features, tags, weight_score):
    n = stochastic_gradient_descent_theta.called % len(features)
    return -tags[n]*features[n]*theta_function(-tags[n]*np.dot(features[n], weight_score))

def theta_function(s):
    if s>0:
        return 1.0/(1.0+np.exp(-s))
    else:
        return np.exp(s)/(1.0+np.exp(s))
