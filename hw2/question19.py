import numpy as np
from hw2.utilities import train_decision_stump, get_config

def main():
    train_path, = get_config('train_path')
    best_of_best = train_decision_stump(train_path)
    print best_of_best

if __name__ == '__main__':
    main()
