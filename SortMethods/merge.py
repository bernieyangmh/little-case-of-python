"""
归并排序

思想：
将一个乱序列分割一半，再将子序列分割一半，直至子序列只含1个或两个元素
将最小子序列排序，再反回父序列，直至返回总序列
14，12，15，13，11，16               ↓
14，12，15    13，11，16             ↓
14，12   15      13，11，  16        ↓
12，14   15      11，13，  16        ↓
12，14，15，       11，13，16         ↓
11，12，13，14，15，16                ↓


split each element into partitions of size 1

recursively merge adjancent partitions

  for i = leftPartStartIndex to rightPartLastIndex inclusive

    if leftPartHeadValue <= rightPartHeadValue

      copy leftPartHeadValue

    else: copy rightPartHeadValue

copy elements back to original array

平均时间O(Nlog2N) 最短时间O(Nlog2N) 最长时间O(Nlog2N) 空间O(n) 稳定
"""


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    seq = [4, 5, 7, 9, 7, 5, 1, 0, 7, -2, 3, -99, 6]
    print(merge_sort(seq))