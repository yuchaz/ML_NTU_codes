from hw4.utilities import get_err_with_different_lambda
from pkg.utilities import load_file

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA_RANGE = range(-10,3)

def main():
    features, tags = load_file(TRAIN_PATH)
    lbda_min = get_err_with_different_lambda(features, tags, features, tags, LAMBDA_RANGE)
    print lbda_min

if __name__ == '__main__':
    main()
