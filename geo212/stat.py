from typing import List, Dict
from .algorithm import merge_sort

__all__ = [
    'mode',
    'frequency',
    'average',
    'median',
    'standard_deviation',
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
    return average((data - avg)**2) * n/(n-1)


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