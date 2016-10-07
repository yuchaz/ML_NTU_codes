import numpy as np
from hw2.utilities import train_decision_stump, get_config

def main():
    train_path, = get_config('train_path')
    Ein_min, min_s, min_theta, min_dimension = train_decision_stump(train_path)
    print 'the best of best Ein is {0}, with s={1}, theta={2}, i={3}'.format(
        Ein_min, min_s, min_theta, min_dimension)

if __name__ == '__main__':
    main()
