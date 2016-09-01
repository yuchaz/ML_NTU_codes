import utilities as util

DATA_PATH = 'hw1_15_train.dat'
TRAIN_TIMES = 2000

def main():
    features, decisions = util.load_file(DATA_PATH)
    cycles_list, average_of_cycles = util.random_train (
        features, decisions, TRAIN_TIMES)

    print average_of_cycles

    util.create_histogram(
        cycles_list,
        hist_title=r'$\mathrm{Random\ PLA\ with\ }\eta = 1$',
        x_label='# of Cycles')


if __name__ == '__main__':
    main()
