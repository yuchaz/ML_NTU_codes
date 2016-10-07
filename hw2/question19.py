from pkg.utilities import load_file
import numpy as np
from hw2.utilities import find_min_Ein

TRAIN_PATH = 'data/hw2_train.dat'
TEST_PATH = 'data/hw2_train.dat'
def main():
    orig_x, y = load_file(TRAIN_PATH, False)
    x = np.transpose(orig_x)
    best_model_list = []
    for i in range(len(x)):
        best_model = find_min_Ein(x[i], y)+(i,)
        best_model_list.append(best_model)

    np.random.shuffle(best_model_list)
    best_of_best = min(best_model_list, key=lambda best:best[0])

    print best_of_best

if __name__ == '__main__':
    main()
