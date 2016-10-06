import numpy as np
from pkg import utilities as util
from hw2.utilities import generate_data, get_config

def main():
    Ein_list = []
    loop_time, data_size, flipping_prob = get_config()
    for rgn in range(loop_time):
        x, y, split_point = generate_data(data_size, flipping_prob)
        theta_position_list = [i-split_point for i in x]
        Ein_min = 1.1
        min_theta = -1.1
        min_s = 0
        err = 0
        for theta in theta_position_list:
            for s in range (-1,3,2):
                for n in range(len(x)):
                    if s*util.sign(x[n]-theta) != y[n]:
                        err += 1
                Ein = 1.0 * err / (data_size*2)
                if Ein <= Ein_min:
                    Ein_min = Ein
                    min_s = s
                    min_theta = theta
        Ein_list.append(Ein_min)
    print np.average(Ein_list)
    util.create_histogram(Ein_list)

if __name__ == '__main__':
    main()
