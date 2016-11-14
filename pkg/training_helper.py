import numpy as np

UPDATE_TIMES = 2000

def train_by_gradient_descent(features, tags, gradient_func, eta=1, update_times=UPDATE_TIMES):
    weight_score = np.zeros(len(features[0]))
    for i in range(update_times):
        gradient = gradient_func(features, tags, weight_score)
        if gradient.all() == 0:
            break
        weight_score = np.add(weight_score, -eta*gradient)
    return weight_score
