"""
冒泡排序

思想
升序排列：选取第一个数与下一个数做比较，大于则交换位置，直到小于下一个数或已到最后
已到最后则再从当前第一个数开始。
若小于下一个数，已下一个数为开始

do

  swapped = false

  for i = 1 to indexOfLastUnsortedElement

    if leftElement > rightElement

      swap(leftElement, rightElement)

      swapped = true

while swapped

平均时间O(n**2) 最短时间O(n) 最长时间O(n**2) 空间O(1) 稳定
"""