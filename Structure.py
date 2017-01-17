# -*- coding: utf-8 -*-

import ctypes


"""
An illustration of the three steps for “growing” a dynamic array:
    (a) create new array B;
    (b) store elements of A in B;
    (c) reassign reference A to the new array.
"""


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                               # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)                         # new (bigger) array
        for k in range(self._n):                        # for each existing value
            B[k] = self._A[k]
        self._A = B                                     # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):         # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None             # help garbage collection
                self._n -= 1
                return
        raise ValueError('value not found')

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        for j in range(self._n, k, -1):                 # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                              # store newest element
        self._n += 1





DynamicArray_summary = """
    Let us assume that one cyber-dollar is enough to pay for the execution of each append operation in S, excluding
the time spent for growing the array. Also, let us assume that growing the array from size k to size 2k requires k
cyber-dollars for the time spent initializing the new array. We shall charge each append operation three cyber-dollars.
Thus, we overcharge each append operation that does not cause an overflow by two cyber-dollars. Think of the two
cyber-dollars profited in an insertion that does not grow the array as being “stored” with the cell in which the element
was inserted. An overflow occurs when the array S has 2i elements, for some integer i ≥ 0, and the size of the array
used by the array representing S is 2i. Thus, doubling the size of the array will require 2i cyber-dollars. Fortunately,
these cyber-dollars can be found stored in cells 2i−1 through 2i − 1. (See Figure 5.14.) Note that the previous overflow
occurred when the number of elements became larger than 2i−1 for the first time, and thus the cyber-dollars stored in
cells 2i−1 through 2i − 1 have not yet been spent. Therefore, we have a valid amortization scheme in which each
operation is charged three cyber-dollars and all the computing time is paid for. That is, we can pay for the execution
of n append operations using 3n cyber-dollars. In other words, the amortized running time of each append operation is
O(1); hence, the total running time of n append operations is O(n).
"""



