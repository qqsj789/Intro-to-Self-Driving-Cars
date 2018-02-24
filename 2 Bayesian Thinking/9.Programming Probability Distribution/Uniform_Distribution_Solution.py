def probability_uniform(low_range, high_range, minimum, maximum):

    ## Calculate the probability of an event occurring between
    ##     low_range and high_range.

    probability = (high_range - low_range) / (maximum - minimum)

    return probability
