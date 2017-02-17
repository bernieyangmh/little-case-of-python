"""
快速排序

思想：
以一个数作基准，小的在左，大的在右
直至左右区间只有一个数


for each (unsorted) partition

  set first element as pivot

  storeIndex = pivotIndex + 1

  for i = pivotIndex + 1 to rightmostIndex

    if element[i] < element[pivot]

      swap(i, storeIndex); storeIndex++

  swap(pivot, storeIndex - 1)

平均时间O(Nlog2N) 最短时间O(Nlog2N) 最长时间O(n**2) 空间O(Nlog2N) 不稳定
"""


def sub_sort(s, low, high):
    """
    将比key小的放左，大的放右
    """
    key = s[low]
    while low < high:
        while low < high and s[high] >= key:
            high -= 1
        while low < high and s[high] < key:
            s[low] = s[high]
            low += 1
            s[high] = s[low]
    s[low] = key
    return low


def quick_sort(s, low, high):
    """

    :param s:
    :param low:     0
    :param high:    s的最?右index
    :return:
    """
    if low < high:
        key_index = sub_sort(s, low, high)
        quick_sort(s, low, key_index)
        quick_sort(s, key_index + 1, high)


if __name__ == '__main__':
    s = [8, 10, 9, 6, 4, 16, 5, 13, 26, 18, 2, 45, 34, 23, 1, 7, 3]
    print(s)
    quick_sort(s, 0, len(s) - 1)
    print(s)

