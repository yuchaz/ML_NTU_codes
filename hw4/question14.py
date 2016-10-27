from hw4.utilities import run_ridge_regression
from pkg.utilities import load_file
from pkg.testing_helper import test_data_from_hypothesis
from pkg.error_estimation import one_zero_error
import matplotlib.pyplot as plt

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA_RANGE = [10**i for i in range(-10,3)]

def main():
    features, tags = load_file(TRAIN_PATH)

    Ein_list = []
    Ein_min = 1
    lbda_min = 0
    for lbda in LAMBDA_RANGE:
        weight_regression = run_ridge_regression(features, tags, lbda)
        Ein = test_data_from_hypothesis(features, tags, weight_regression, one_zero_error)
        Ein_list.append(Ein)
        if Ein < Ein_min:
            Ein_min = Ein
            lbda_min = lbda

    plt.plot(range(-10,3), Ein_list)
    plt.show()
    print lbda_min

if __name__ == '__main__':
    main()
