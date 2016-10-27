from hw4.utilities import get_err_with_different_lambda
from pkg.utilities import load_file

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA_RANGE = range(-10,3)

def main():
    features, tags = load_file(TRAIN_PATH)
    features_to_test, tags_to_test = load_file(TEST_PATH)
    lbda_min, Eout_min = get_err_with_different_lambda(features, tags, features_to_test, tags_to_test, LAMBDA_RANGE)
    print 'Eout min is {0}, occurred at log(lambda) = {1}'.format(Eout_min, lbda_min)

if __name__ == '__main__':
    main()
