def bar_heights(intervals, probabilities, total_probability):

    heights = []

    total_relative_prob = sum(probabilities)

    for i in range(0, len(probabilities)):
        bar_area = (probabilities[i] / total_relative_prob) * total_probability
        heights.append(bar_area / (intervals[i + 1] - intervals[i]))

    return heights
