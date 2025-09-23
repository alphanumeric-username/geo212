from typing import List


def merge_sort(data: List[int|float]) -> List[int|float]:
    """
    Sorts a list of numbers using the merge sort algorithm.

    Parameters
    ----------
    data : List[int|float]
        The list of numbers whose modes will be calculated.
    
    Returns
    -------
    A new list with the same elements of `data`, but sorted.
    """
    if len(data) == 1:
        return data
    if len(data) == 2:
        return [min(data), max(data)]
    
    n = len(data)
    left_sort = merge_sort(data[:n//2])
    right_sort = merge_sort(data[n//2:])
    partial_sort = []
    while len(left_sort) > 0 or len(right_sort) > 0:
        if len(left_sort) == 0:
            while len(right_sort) > 0:
                partial_sort.append(right_sort.pop(0))
        elif len(right_sort) == 0:
            while len(left_sort) > 0:
                partial_sort.append(left_sort.pop(0))
        else:
            if left_sort[0] < right_sort[0]:
                partial_sort.append(left_sort.pop(0))
            else:
                partial_sort.append(right_sort.pop(0))
    
    return partial_sort