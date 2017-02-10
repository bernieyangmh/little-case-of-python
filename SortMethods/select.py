"""
选择排序

思想：
共重复元素的数量－1次
每次挑选最小的数放在对应的索引上，然后考虑之后的元素
例如对于[3,5,2,1,0,8]
挑选0放在第一个，然后挑选1放在第二个，2放在第三个......

repeat (numOfElements - 1) times

  set the first unsorted element as the minimum

  for each of the unsorted elements

    if element < currentMinimum

      set element as new minimum

  swap minimum with first unsorted position

  平均时间O(n**2) 最短时间O(n**2) 最长时间O(n**2) 空间O(1) 不稳定
"""