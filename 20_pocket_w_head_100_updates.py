import utilities as util
TRAIN_PATH = 'hw1_18_train.dat'
VERIFY_PATH = 'hw1_18_test.dat'
UPDATE_TIMES = 100
LOOP_TIMES = 2000

def main():
    error_rate_list, average_error_rate = util.run_pocket(TRAIN_PATH, VERIFY_PATH, UPDATE_TIMES, LOOP_TIMES)
    print average_error_rate
    util.create_histogram(error_rate_list, hist_title=r'$\mathbf{w}_{POCKET}\  \mathrm{\ after\ updating\ 100\ times}$', x_label='# of Errors')


if __name__ == '__main__':
    main()
