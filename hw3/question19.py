import numpy as np
import pkg.utilities as util
from hw3.utilities import train_by_gradient_descent, batch_gradient_descent_theta, one_zero_error, test_data_from_hypothesis

TRAIN_PATH = 'data/hw3_train.dat'
TEST_PATH = 'data/hw3_test.dat'
UPDATE_TIMES = 2000
eta = 0.01

def main():
    features, tags = util.load_file(TRAIN_PATH, False)
    test_features, test_tags = util.load_file(TEST_PATH, False)
    weight_score_full_gradient = train_by_gradient_descent(features, tags, batch_gradient_descent_theta, eta, UPDATE_TIMES)
    Eout = test_data_from_hypothesis(test_features, test_tags, weight_score_full_gradient, one_zero_error)
    print weight_score_full_gradient
    print Eout
if __name__ == '__main__':
    main()
