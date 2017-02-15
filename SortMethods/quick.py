"""
快速排序

思想：
去一个数作基准，小的在左，大的在右
直至左右只有一个数


for each (unsorted) partition

  set first element as pivot

  storeIndex = pivotIndex + 1

  for i = pivotIndex + 1 to rightmostIndex

    if element[i] < element[pivot]

      swap(i, storeIndex); storeIndex++

  swap(pivot, storeIndex - 1)

平均时间O(Nlog2N) 最短时间O(Nlog2N) 最长时间O(n**2) 空间O(Nlog2N) 不稳定
"""

def quick_sort(lists, left, right):
    if left >= right:
        return lists
    k = lists[left]
    low = left
    hight = right
    while left < right:
        while left < right and lists[right] >= k:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[right] <= k:
            left += 1
        lists[right] = lists[left]



