import numpy as np

def run_ridge_regression(features, tags, lambda_v):
    z_square = np.dot(np.transpose(features),features)
    z_square_plus_reg_term = z_square + np.identity(len(z_square))*lambda_v
    pseudo_inverse_z = np.dot(np.linalg.inv(z_square_plus_reg_term),np.transpose(features))
    w_reg = np.dot(pseudo_inverse_z,tags)
    return w_reg
