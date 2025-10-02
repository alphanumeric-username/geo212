from typing import List, Dict
from geo212.algorithm import merge_sort


__all__ = [
    'mode',
    'frequency',
    'average',
    'median',
    'standard_deviation',
    'covariance',
    'correlation'
]

def mode(data: List[int|float]) -> List[int|float]:
    """
    Computes the modes of a list of numbers.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose modes will be calculated.
    
    Returns
    -------
    A list containing the modes of the list.
    """
    freq = {}
    most_frequent = None
    greatest_frequency = 0
    most_frequent_set = {}
    
    for i in range(len(data)):
        if data[i] not in freq:
            freq[data[i]] = 1
        else:
            freq[data[i]] += 1

        if most_frequent is None:
            most_frequent = data[i]
            greatest_frequency = 1
            most_frequent_set = {data[i]}
        elif freq[data[i]] == greatest_frequency:
            most_frequent = data[i]
            most_frequent_set.add(data[i])
        elif greatest_frequency < freq[data[i]]:
            most_frequent = data[i]
            most_frequent_set = {data[i]}
            greatest_frequency = freq[data[i]]
        
    return list(most_frequent_set)


def frequency(data: List[int|float]) -> Dict[int|float, int]:
    """
    Counts how often each element of a given list appears.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose elements frequency will be calculated.

    Returns
    -------
    A dictionary whose keys are the unique elements of `data` and its
    values are their frequency.
    """
    freq = {}

    for i in range(len(data)):
        if data[i] not in freq:
            freq[data[i]] = 1
        else:
            freq[data[i]] += 1
    
    return freq


def average(data: List[int|float]) -> int|float:
    """
    Computes the average of a list of numbers.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose average will be calculated.
    
    Returns
    -------
    The average.
    """
    sum = 0
    n = len(data)
    if n == 0:
        return 0
    for i in range(n):
        sum += data[i]
    return sum/n


def median(data: List[int|float]) -> int|float:
    """
    Computes the median of a list of numbers.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose median will be calculated.
    
    Returns
    -------
    The median of the list.
    """
    sorted_data = merge_sort(list(data))
    n = len(sorted_data)
    if n % 2 == 1:
        return sorted_data[(n + 1)//2 - 1]
    else:
        return (sorted_data[n//2 - 1] + sorted_data[n//2])/2
    

def variance(data: List[int|float]) -> int|float:
    """
    Computes the variance of a list of numbers.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers variance will be calculated.

    Returns
    -------
    The variance of the list of numbers.
    """
    n = len(data)
    avg = average(data)
    return average([(d - avg)**2 for d in data]) * n/(n-1)


def standard_deviation(data: List[int|float]) -> int|float:
    """
    Computes the standard deviation of a list of numbers.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose standard deviation will be calculated.
    
    Returns
    -------
    The standard deviation of the list of numbers.
    """
    variance(data)**.5


def covariance(data_x: List[int|float], data_y: List[int|float]) -> float|int:
    """
    Computes the covariance between two lists of numbers.

    Parameters
    ----------
    data_x : List[int|float]
        The first list. Must have the same length as `data_y`
    data_y : List[int|float]
        The second list. Must have the same length as `data_x`

    Returns
    -------
    The covariance between `data_x` and `data_y`.
    """
    if len(data_x) != len(data_y):
        raise ValueError(f'`data_x` and `data_y` does not have the same length:\
                          `data_x` has length {len(data_x)} while `data_y` has length {len(data_y)}')

    n = len(data_x)
    Ex = average(data_x)
    Ey = average(data_y)

    return average([ (x - Ex)*(y - Ey) for x, y in zip(data_x, data_y) ]) * n/(n-1)


def correlation(data_x: List[int|float], data_y: List[int|float]) -> float|int:
    """
    Computes the correlation between two lists of numbers.

    Parameters
    ----------
    data_x : List[int|float]
        The first list. Must have the same length as `data_y`
    data_y : List[int|float]
        The second list. Must have the same length as `data_x`

    Returns
    -------
    The correlation between `data_x` and `data_y`.
    """
    sx = standard_deviation(data_x)
    sy = standard_deviation(data_y)
    return covariance(data_x, data_y)/(sx * sy)


def correlation_matrix(data: Dict[str, List[int | float]]):
    keys = list(data.keys())
    n = len(keys)
    # MCor = np.zeros((n, n))
    MCor = [[ 0 for i in range(n)] for j in range(n)]

    for c in range(len(keys)):
        for r in range(len(keys)):
            kx = keys[r]
            ky = keys[c]
            MCor[r, c] = correlation(data[kx], data[ky])

    return MCor
