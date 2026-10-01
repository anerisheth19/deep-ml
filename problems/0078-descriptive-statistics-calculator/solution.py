import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    res = {}
    mean = np.mean(data)
    low = 0
    high = len(data) - 1
    mid = (low + high) // 2
    if len(data) % 2 == 1:
        median = data[mid]
    else:
        median = (data[mid] + data[mid+1])/2

    max_count = 0
    counts = {}
    for i in data:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    mode = 0
    for value in counts:
        if counts[value] > max_count:
            max_count = counts[value]
            mode = value
    
    variance = 0
    sum_var = 0
    for i in data:
        sum_var += (i - mean) * (i - mean)
    variance = sum_var / len(data)
    standard_deviation = np.sqrt(variance)
     
    if len(data) == 1:
        q1 = q2 = q3 = data[0]
    else:
        quarter1 = 0.25 * (len(data)-1)
        quarter2 = 0.5 * (len(data)-1)
        quarter3 = 0.75 * (len(data)-1)

        lower1 = int(quarter1)
        fraction1 = quarter1 - lower1
        lower2 = int(quarter2)
        fraction2 = quarter2 - lower2
        lower3 = int(quarter3)
        fraction3 = quarter3 - lower3

        q1 = data[lower1] + fraction1 * (data[lower1+1] - data[lower1])
        q2 = data[lower2] + fraction2 * (data[lower2+1] - data[lower2])
        q3 = data[lower3] + fraction3 * (data[lower3+1] - data[lower3])

    res["mean"] = mean
    res["median"] = median
    res["mode"] = mode
    res["variance"] = variance
    res["standard_deviation"] = standard_deviation
    res['25th_percentile']= q1
    res['50th_percentile']= q2
    res['75th_percentile']= q3
    res['interquartile_range']= res['75th_percentile'] - res['25th_percentile']
    
    return res
    # Your code here
    pass