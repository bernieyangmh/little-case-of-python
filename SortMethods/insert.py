"""
插入排序

思想：
遍历一遍，每次选择相应索引上的值，第一次选第一个，第二次选第二个。
将其与前面的数依次比较，直至小于某个数a，将其插入其后，原来a之后的每个元素索引＋1

mark first element as sorted

for each unsorted element

  'extract' the element

  for i = lastSortedIndex to 0

    if currentSortedElement > extractedElement

      move sorted element to the right by 1

    else: insert extracted element

平均时间O(n**2) 最短时间O(n) 最长时间O(n**2) 空间O(1) 稳定


"""


def insertion_sort(s):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(s)):
        cur = s[k]                          # 建立游标
        j = k                               # 拿到当前游标值
        while j > 0 and s[j-1] > cur:       # 当前一位值大于游标的值
            s[j] = s[j-1]                   # 交换位置
            j -= 1                          # 游标向前移
        s[j] = cur                          # 获取游标值


s = [3, 5, 1, 2, 7, 6, 3, 0, 9]
insertion_sort(s)
print(s)



