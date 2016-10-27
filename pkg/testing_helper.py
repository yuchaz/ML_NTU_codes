def test_data_from_hypothesis(features, tags, weight_score, error_measure_function):
    err = 0
    for n in range(len(tags)):
        if error_measure_function(features[n], tags[n], weight_score) == True:
            err += 1

    Err = float(err) / len(features)
    return Err
