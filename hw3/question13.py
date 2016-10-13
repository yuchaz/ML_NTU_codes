from pkg import utilities as util
from hw3.utilities import generate_data, run_linear_regression, add_constant_term
import numpy as np

DATA_SIZE = 1000
FLIPPING_PROB = 0.1
LOOP_TIMES = 1000

def main():
    Ein_list = []
    for i in range(LOOP_TIMES):
        x, y = generate_data(DATA_SIZE,FLIPPING_PROB)
        x_with_const_term = add_constant_term(x)
        w_lin = run_linear_regression(x_with_const_term, y)
        err = 0
        for n in range(len(x)):
            if util.same_sign(np.dot(w_lin, x_with_const_term[n]), y[n]) == False:
                err += 1
        Ein = float(err) / len(x)
        Ein_list.append(Ein)

    print np.average(Ein_list)
    util.create_histogram(Ein_list)


if __name__ == '__main__':
    main()
