# 17_1D_decision_stump_plot_Ein
import numpy as np

LOOP_TIME = 5000

LOWER_BOUND = -1
UPPER_BOUND = 1
SPLIT_POINT_PRECISION = 5




def generate_data(data_size, lower_bound=LOWER_BOUND, upper_bound=UPPER_BOUND, split_point_precision=SPLIT_POINT_PRECISION):
    x = np.random.uniform(lower_bound,higher_bound,data_size)


for rgn in range(LOOP_TIME):
    data_size = 20
    x, y, split_point = generate_data(data_size)
    # x, y, theta_position = generate_data(lower_bound, upper_bound, divide_amount, theta_position_lower_than)
    theta_position_list = [i-theta_position for i in x]
    Ein_min = 1.1
    lowest_theta = -1.1
    lowest_s = 0
    for tta in theta_position_list:
        for s in range (-1,3,2):
            for n in range(len(x)):
                err = 0
                if s*sign(x[n]-tta) !== y[n]:
                    err += 1
            Ein = err / divide_amount
            if Ein <= Ein_min:
                Ein_min = Ein
                lowest_s = s
                lowest_theta = tta
