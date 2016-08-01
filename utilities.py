from numpy import array, dot, zeros, add, random, arange, average
import matplotlib.pyplot as plt
import random

def load_file (infile):
    features_of_data = []
    decisions_of_data = []

    with open(infile, 'r') as f:
        for line in f:
            line_list = map(float, line.split())
            x = array([1]+line_list[:-1])
            y = line_list[-1]
            features_of_data.append(x)
            decisions_of_data.append(y)

    return features_of_data, decisions_of_data

def same_sign (a, b):
    if a * b <= 0:
        return False
    else:
        return True

def generate_index_map (length, rand=False):
    index_map = arange(length)
    if rand:
        random.shuffle(index_map)
    return index_map


def train (features, decisions, rand=False, eta=1):
    weight_score = zeros(len(features[0]))
    last_training_index = 0
    loop_cycling_thru = 0
    index_map = generate_index_map(len(features), rand)

    while True:
        if_find_fault = False
        for idx in index_map:
            if same_sign(dot(weight_score, features[idx]),
                         decisions[idx]) == False:
                weight_score = add(
                    weight_score, eta * features[idx] * decisions[idx])
                last_training_index = idx
                if_find_fault = True
                loop_cycling_thru += 1
        if if_find_fault == False:
            break

    return loop_cycling_thru, last_training_index

def run_pocket (
        train_path, verify_path, update_times,
        loop_times, use_w_last=False):
    train_features, train_decisions = load_file(train_path)
    verify_features, verify_decisions = load_file(verify_path)
    error_rate_list = []

    for i in range(loop_times):
        t_weight_score_head, t_weight_score_last = pocket_train(
            train_features, train_decisions, update_times)
        if use_w_last == False:
            trained_weight_score = t_weight_score_head
        else:
            trained_weight_score = t_weight_score_last
        # trained_weight_score = t_weight_score_head if use_w_last == False else t_weight_score_last

        error_rate = pocket_verfity(
            verify_features, verify_decisions, trained_weight_score)
        error_rate_list.append(error_rate)

    return error_rate_list, average(error_rate_list)

def pocket_train (features, decisions, update_times, rand=True):
    weight_score = zeros(len(features[0]))
    weight_score_head = zeros(len(features[0]))
    least_error_num = len(features)
    index_map = generate_index_map(len(features), rand)

    for i in range(update_times):
        error_features_index_list = []
        for idx in index_map:
            if same_sign(dot(weight_score, features[idx]),
                         decisions[idx]) == False:
                error_features_index_list.append(idx)

        if len(error_features_index_list) <= least_error_num:
            weight_score_head = weight_score
            least_error_num = len(error_features_index_list)

        target_index = error_features_index_list[0]
        weight_score = add(
            weight_score,
            features[target_index] * decisions[target_index])

    return weight_score_head, weight_score

def pocket_verfity (features, decisions, weight_score):
    error_count = 0
    for idx in range(len(features)):
        if same_sign(dot(weight_score, features[idx]),
                     decisions[idx]) == False:
            error_count += 1

    error_rate = error_count / float(len(features))
    return error_rate


def random_train (features, decisions, times, eta=1):
    cycles_list = []
    for idx in range(times):
        loop_cycling_thru, lti = train(features, decisions, True, eta)
        cycles_list.append(loop_cycling_thru)

    return cycles_list, average(cycles_list)

def create_histogram (
        list_to_draw, x_label='X Axis',
        hist_title=r'$\mathrm{Histogram}$', hist_color='green'):
    hist_bins = len(list_to_draw)
    plt.hist(list_to_draw, bins=hist_bins, normed=True,
             color=hist_color, histtype='step')

    plt.xlabel(x_label)
    plt.ylabel('Frequency')
    plt.title(hist_title)
    plt.grid(True)

    plt.show()
