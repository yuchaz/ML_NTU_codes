import utilities as util

DATA_PATH = 'hw1_15_train.dat'
TRAIN_TIMES = 2000
ETA = 0.5

def main():
    features, decisions = util.load_file(DATA_PATH)
    cycles_list, average_of_cycles = util.random_train (features, decisions, TRAIN_TIMES, ETA)
    print (average_of_cycles)
    util.create_histogram(cycles_list)

if __name__ == '__main__':
    main()
