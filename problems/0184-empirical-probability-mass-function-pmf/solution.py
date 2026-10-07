def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    counts = {}
    for i in range(len(samples)):
        if samples[i] in counts:
            counts[samples[i]] += 1
        else:
            counts[samples[i]] = 1
    
    res = []
    for key,val in counts.items():
        prob = val / len(samples)
        res.append((key, prob))

    return res
    pass