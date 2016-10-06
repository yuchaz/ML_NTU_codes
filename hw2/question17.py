import numpy as np

LOOP_TIME = 5000
LOWER_BOUND = -1
UPPER_BOUND = 1
SPLIT_POINT_PRECISION = 5
FLIPPING_PROB = 0.2

def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def flip_sign_with_probability(p):
    rand_seed = np.random.ranf()
    if rand_seed >= p:
        return 1
    else:
        return -1

def generate_data(
        data_size, lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND,
        split_point_precision=SPLIT_POINT_PRECISION):
    x = np.random.uniform(lower_bound,upper_bound,data_size)
    y = [sign(i * flip_sign_with_probability(FLIPPING_PROB)) for i in x]
    split_point = (upper_bound - lower_bound)/split_point_precision

    return x, y, split_point


def main():
    Ein_list = []
    for rgn in range(LOOP_TIME):
        data_size = 20
        x, y, split_point = generate_data(data_size)
        theta_position_list = [i-split_point for i in x]
        Ein_min = 1.1
        min_theta = -1.1
        min_s = 0
        err = 0
        for theta in theta_position_list:
            for s in range (-1,3,2):
                for n in range(len(x)):

                    if s*sign(x[n]-theta) != y[n]:
                        err += 1
                Ein = 1.0 * err / (data_size*2)
                if Ein <= Ein_min:
                    Ein_min = Ein
                    min_s = s
                    min_theta = theta

    Ein_list.append(Ein_min)
    print np.average(Ein_list)

if __name__ == '__main__':
    main()
