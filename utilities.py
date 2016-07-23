from numpy import array, dot, zeros, add, random, arange

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


def train (features, decisions, rand=False):
    weight_score = zeros(len(features[0]))
    last_training_index = 0
    loop_cycling_thru = 0
    index_map = generate_index_map(len(features), rand)

    while True:
        if_find_fault = False
        for idx in index_map:
            if same_sign(dot(weight_score, features[idx]), decisions[idx]) == False:
                weight_score = add(weight_score, features[idx] * decisions[idx])
                last_training_index = idx
                if_find_fault = True
                loop_cycling_thru += 1
        if if_find_fault == False:
            break

    return loop_cycling_thru, last_training_index
