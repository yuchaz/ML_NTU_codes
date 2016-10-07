import numpy as np
from pkg import utilities as util
import ConfigParser

LOWER_BOUND = -1
UPPER_BOUND = 1
SPLIT_POINT_PRECISION = 5
SPLIT_POINT_DEFAULT = 0.0000001

def generate_data(
        data_size, flipping_prob,
        lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND,
        split_point_precision=SPLIT_POINT_PRECISION):
    x = np.random.uniform(lower_bound,upper_bound,data_size)
    y = [util.sign(i * util.flip_sign_with_probability(flipping_prob)) for i in x]
    split_point = float(upper_bound - lower_bound)/data_size/split_point_precision

    return x, y, split_point

def get_config(*arg):
    config = ConfigParser.RawConfigParser()
    config.read('hw2/config.ini')

    return [config.get('one_dimensional_perceptron', i) for i in arg]

def find_min_Ein(x, y, split_point=SPLIT_POINT_DEFAULT):
    theta_position_list = [i-split_point for i in x]
    Ein_min = 1.1
    min_theta = -1.1
    min_s = 0
    err = 0
    data_size = len(x)
    for theta in theta_position_list:
        for s in range (-1,3,2):
            for n in range(len(x)):
                if s*util.sign(x[n]-theta) != y[n]:
                    err += 1
            Ein = float(err) / (data_size*2)
            if Ein <= Ein_min:
                Ein_min = Ein
                min_s = s
                min_theta = theta
    return Ein_min, min_s, min_theta

def train_decision_stump(path):
    orig_x, y = util.load_file(path, False)
    x = np.transpose(orig_x)
    best_model_list = []
    for i in range(len(x)):
        best_model = find_min_Ein(x[i], y)+(i,)
        best_model_list.append(best_model)

    np.random.shuffle(best_model_list)
    return min(best_model_list, key=lambda best:best[0])
