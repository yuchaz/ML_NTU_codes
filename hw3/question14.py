from pkg import utilities as util
from hw3.utilities import generate_data, run_linear_regression, quadratic_transform_for_dim_2
import numpy as np

DATA_SIZE = 1000
FLIPPING_PROB = 0.1
LOOP_TIMES = 1000

def main():
    Ein_list = []
    for i in range(LOOP_TIMES):
        x, y = generate_data(DATA_SIZE,FLIPPING_PROB)
        transformed_z = quadratic_transform_for_dim_2(x)

        w_lin = run_linear_regression(transformed_z, y)
        err = 0
        for n in range(len(y)):
            if util.same_sign(np.dot(w_lin, transformed_z[n]), y[n]) == False:
                err += 1
        Ein = float(err) / len(y)
        Ein_list.append(Ein)

    print np.average(Ein_list)
    util.create_histogram(Ein_list)


if __name__ == '__main__':
    main()
