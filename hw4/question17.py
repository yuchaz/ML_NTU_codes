from hw4.utilities import get_err_with_different_lambda
from pkg.utilities import load_file

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA_RANGE = range(-10,3)

def main():
    features, tags = load_file(TRAIN_PATH)
    features_to_train, features_to_test = features[0:120], features[120:]
    tags_to_train, tags_to_test = tags[0:120], tags[120:]
    lbda_min, Eval_min = get_err_with_different_lambda(features_to_train, tags_to_train, features_to_test, tags_to_test, LAMBDA_RANGE)
    print 'Eval min is {0}, occurred at log(lambda) = {1}'.format(Eval_min, lbda_min)

if __name__ == '__main__':
    main()
