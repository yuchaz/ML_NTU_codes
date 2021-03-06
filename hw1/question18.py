# Q18_pocket_w_head
from pkg import utilities as util
TRAIN_PATH = 'data/hw1_18_train.dat'
VERIFY_PATH = 'data/hw1_18_test.dat'
UPDATE_TIMES = 50
LOOP_TIMES = 2000

def main():
    error_rate_list, average_error_rate = util.run_pocket(
        TRAIN_PATH, VERIFY_PATH,
        UPDATE_TIMES, LOOP_TIMES)

    print average_error_rate

    util.create_histogram(
        error_rate_list,
        hist_title=r"$\mathbf{w}_{POCKET}\ "
                   r"\mathrm{\ after\ updating\ 50\ times}$",
        x_label='# of Errors')


if __name__ == '__main__':
    main()
