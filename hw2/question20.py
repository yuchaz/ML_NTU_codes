import numpy as np
from hw2.utilities import train_decision_stump, get_config
import pkg.utilities as util

def main():
    train_path, test_path = get_config('train_path', 'test_path')
    ein, min_s, min_theta, min_dimension = train_decision_stump(train_path)
    x_test, y_test = util.load_file(test_path, False)
    err = 0
    for n in range(len(x_test)):
        if min_s*util.sign(x_test[n][min_dimension]-min_theta) != y_test[n]:
            err += 1
    E_test = float(err) / len(x_test)
    print E_test

if __name__ == '__main__':
    main()
