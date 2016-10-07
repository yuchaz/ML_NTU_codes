import numpy as np
from pkg import utilities as util
from hw2.utilities import generate_data, get_config

def main():
    Eout_list = []
    loop_time, data_size, flipping_prob = get_config('loop_time', 'data_size', 'flipping_prob')

    for rgn in range(int(loop_time)):
        x, y, sp = generate_data(int(data_size), float(flipping_prob))
        ideal_y = [util.sign(i) for i in x]
        err = 0
        for n in range(len(y)):
            if y[n] != ideal_y[n]:
                err += 1
        Eout = float(err) / len(y)
        Eout_list.append(Eout)

    print np.average(Eout_list)
    util.create_histogram(Eout_list)


if __name__ == '__main__':
    main()
