from pkg import utilities as util
from hw3.utilities import generate_data, run_quadratic_regression, quadratic_transform_for_dim_2
import numpy as np

DATA_SIZE = 1000
FLIPPING_PROB = 0.1
LOOP_TIMES = 1000

def main():
    Eout_list = []
    w3_list = []
    for i in range(LOOP_TIMES):
        x, y = generate_data(DATA_SIZE,FLIPPING_PROB)
        w_qua, tz = run_quadratic_regression(x,y)

        x_out_sample, y_out_sample = generate_data(DATA_SIZE,FLIPPING_PROB)
        transformed_z_out = quadratic_transform_for_dim_2(x_out_sample)

        err = 0
        for n in range(len(y)):
            if util.same_sign(np.dot(w_qua, transformed_z_out[n]), y_out_sample[n]) == False:
                err += 1
        Eout = float(err) / len(y)
        Eout_list.append(Eout)


    print np.average(Eout_list)
    util.create_histogram(Eout_list)


if __name__ == '__main__':
    main()
