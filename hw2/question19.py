import numpy as np
from hw2.utilities import train_decision_stump

TRAIN_PATH = 'data/hw2_train.dat'
TEST_PATH = 'data/hw2_train.dat'
def main():
    best_of_best = train_decision_stump(TRAIN_PATH)
    print best_of_best

if __name__ == '__main__':
    main()
