import numpy as np
import pkg.utilities as util

def one_zero_error(feature, tag, weight_score):
    return util.same_sign(np.dot(weight_score, feature), tag) == False
