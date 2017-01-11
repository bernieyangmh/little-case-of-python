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

"""
    To prove this claim, a crucial fact is that with each recursive call the number of candidate entries still to be
searched is given by the value
                                            high−low+1
Moreover, the number of remaining candidates is reduced by at least one half
with each recursive call. Specifically, from the definition of mid, the number of remain- ing candidates is either

                                (mid−1)−low+1 = └low+high┘/2 − low <= (high−low+1)/2
                    or
                                high−(mid+1)+1 = high − └low+high┘/2 <= (high−low+1)/2

    Initially, the number of candidates is n; after the first call in a binary search, it is at most n/2; after the
second call, it is at most n/4; and so on. In general, after the jth call in a binary search, the number of candidate
entries remaining is at most n/2**j. In the worst case (an unsuccessful search), the recursive calls stop when there are
no more candidate entries. Hence, the maximum number of recursive calls performed, is the smallest integer r such that

                                n/2**r < 1
    In other words (recalling that we omit a logarithm’s base when it is 2), r > log n.
Thus, we have
                                r = └logN┘ + 1

which implies that binary search runs in O(logN) time.
"""