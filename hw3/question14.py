from pkg import utilities as util
from hw3.utilities import generate_data, run_linear_regression, run_quadratic_regression, generate_data_and_run_regression
import numpy as np

DATA_SIZE = 1000
FLIPPING_PROB = 0.1
LOOP_TIMES = 1000

def main():
    Ein_list = []
    w3_list = []
    for i in range(LOOP_TIMES):
        w_qua, Ein = generate_data_and_run_regression(DATA_SIZE, FLIPPING_PROB)
        Ein_list.append(Ein)
        w3_list.append(w_qua[3])

    print np.average(w3_list)
    util.create_histogram(w3_list)


if __name__ == '__main__':
    main()
