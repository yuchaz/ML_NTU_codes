from hw4.utilities import calculate_err_with_different_lambda, plot_x_y
from pkg.utilities import load_file
import numpy as np

TRAIN_PATH = 'data/hw4_train.dat'
TEST_PATH = 'data/hw4_test.dat'
LAMBDA_RANGE = range(-10,3)
FOLDS_TO_CREATE = 5

def main():
    features, tags = load_file(TRAIN_PATH)
    features_folds = [features[i:i+len(features)/5] for i in xrange(0,len(features), len(features)/5)]
    tags_folds = [tags[i:i+len(tags)/5] for i in xrange(0,len(tags), len(tags)/5)]
    Ecv_list = [[]]*FOLDS_TO_CREATE
    for i in range(FOLDS_TO_CREATE):
        features_to_train = [e for idx in range(FOLDS_TO_CREATE) if idx != i for e in features_folds[idx]]
        features_to_test = features_folds[i]
        tags_to_train = [ e for idx in range(FOLDS_TO_CREATE) if idx != i for e in tags_folds[idx]]
        tags_to_test = tags_folds[i]

        Ecvmin, Ecvs, lbdamin = calculate_err_with_different_lambda(features_to_train, tags_to_train, features_to_test, tags_to_test, LAMBDA_RANGE)
        Ecv_list[i].append(Ecvs)

    Ecv_trans = np.array(Ecv_list).transpose()
    Ecv_output = [np.average(e) for e in Ecv_trans]
    plot_x_y(LAMBDA_RANGE, Ecv_output)
    print 'Eval min is {0}, occurred at log(lambda) = {1}'.format(np.amin(Ecv_output), LAMBDA_RANGE[Ecv_output.index(np.amin(Ecv_output))])

if __name__ == '__main__':
    main()
