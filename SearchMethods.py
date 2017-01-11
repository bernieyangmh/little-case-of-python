# -*- coding: utf-8 -*-

def binary_search(data, target, low, high):
    """
    Return True if target is found in indicated portion of a Python list.
    The search only considers the portion from data[low] to data[high] inclusive.

    We consider three cases:
    1.If the target equals data[mid], then we have found the item we are looking for, and the search terminates successfully.
    2.If target < data[mid], then we recur on the first half of the sequence, that is, on the interval of indices from low to mid − 1.
    3.If target > data[mid], then we recur on the second half of the sequence, that is, on the interval of indices from mid + 1 to high.

    runs in O(n) time, not good.The next method  runs in O(logn) time,
    """

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)

        else:
            return binary_search(data, target, mid+1, high)
