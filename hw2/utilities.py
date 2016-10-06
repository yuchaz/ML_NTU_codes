import numpy as np
from pkg import utilities as util
import ConfigParser

LOWER_BOUND = -1
UPPER_BOUND = 1
SPLIT_POINT_PRECISION = 5

def generate_data(
        data_size, flipping_prob,
        lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND,
        split_point_precision=SPLIT_POINT_PRECISION):
    x = np.random.uniform(lower_bound,upper_bound,data_size)
    y = [util.sign(i * util.flip_sign_with_probability(flipping_prob)) for i in x]
    split_point = (upper_bound - lower_bound)/split_point_precision

    return x, y, split_point

def get_config():
    config = ConfigParser.RawConfigParser()
    config.read('hw2/config.ini')
    loop_time = int(config.get('one_dimensional_perceptron', 'loop_time'))
    data_size = int(config.get('one_dimensional_perceptron', 'data_size'))
    flipping_prob = float(config.get('one_dimensional_perceptron', 'flipping_prob'))
    return loop_time, data_size, flipping_prob
