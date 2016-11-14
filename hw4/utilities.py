import numpy as np
import matplotlib.pyplot as plt
from pkg.testing_helper import test_data_from_hypothesis
from pkg.error_estimation import one_zero_error

def run_ridge_regression(features, tags, lambda_v):
    z_square = np.dot(np.transpose(features),features)
    z_square_plus_reg_term = z_square + np.identity(len(z_square))*lambda_v
    pseudo_inverse_z = np.dot(np.linalg.inv(z_square_plus_reg_term),np.transpose(features))
    w_reg = np.dot(pseudo_inverse_z,tags)
    return w_reg

def calculate_err_with_different_lambda(fea_to_train, tag_to_train, fea_to_test, tag_to_test, lambda_range):
    Err_list = []
    Err_min = 1
    lbda_min = 0
    lambda_list = [10**i for i in lambda_range]
    for lbda in lambda_list:
        weight_regression = run_ridge_regression(fea_to_train, tag_to_train, lbda)
        Err = test_data_from_hypothesis(fea_to_test, tag_to_test, weight_regression, one_zero_error)
        Err_list.append(Err)
        if Err < Err_min:
            Err_min = Err
            lbda_min = lbda
    return Err_min, Err_list, lbda_min

def get_err_with_different_lambda(fea_to_train, tag_to_train, fea_to_test, tag_to_test, lambda_range):
    Err_min, Err_list, lbda_min = calculate_err_with_different_lambda(fea_to_train, tag_to_train, fea_to_test, tag_to_test, lambda_range)
    plot_x_y(lambda_range, Err_list)
    return np.log10(lbda_min), Err_min


def plot_x_y(x_list,y_list):
    plt.plot(x_list, y_list)
    plt.show()
