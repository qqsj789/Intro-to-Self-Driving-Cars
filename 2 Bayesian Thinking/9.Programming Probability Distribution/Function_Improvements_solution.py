def probability_range_improved(low_range, high_range, minimum, maximum):

    if (isinstance(low_range, str) or isinstance(high_range, str)):
        # print a message to the user and return none
        print('Inputs should be numbers not string')
        return None

    if (low_range < minimum or low_range > maximum):
        # print a message to the user and return none
        print('Your low range value must be between minimum and maximum')
        return None

    if (high_range < minimum or high_range > maximum):
        # print a message to the user and return none
        print('The high range value must be between minimum and maximum')
        return None

    probability = abs(high_range - low_range) / (maximum - minimum)

    return probability
