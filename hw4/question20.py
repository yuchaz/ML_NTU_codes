from hw4.utilities import run_ridge_regression
from pkg.utilities import load_file
from pkg.testing_helper import test_data_from_hypothesis
from pkg.error_estimation import one_zero_error

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA = 10**-8

def main():
    features, tags = load_file(TRAIN_PATH)
    test_features, test_tags = load_file(TEST_PATH)
    weight_regression = run_ridge_regression(features, tags, LAMBDA)
    Ein = test_data_from_hypothesis(features, tags, weight_regression, one_zero_error)
    Eout = test_data_from_hypothesis(test_features, test_tags, weight_regression, one_zero_error)
    print 'Ein is {0}, and Eout is {1}'.format(Ein, Eout)

if __name__ == '__main__':
    main()
