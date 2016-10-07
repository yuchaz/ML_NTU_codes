import numpy as np
from pkg import utilities as util
from hw2.utilities import generate_data, get_config, find_min_Ein

def main():
    Ein_list = []
    loop_time, data_size, flipping_prob = get_config()
    for rgn in range(loop_time):
        x, y, split_point = generate_data(data_size, flipping_prob)
        Ein_min, ms, mt = find_min_Ein(x,y,split_point)
        Ein_list.append(Ein_min)
    print np.average(Ein_list)
    util.create_histogram(Ein_list)

if __name__ == '__main__':
    main()
