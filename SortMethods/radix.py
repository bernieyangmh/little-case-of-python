"""
桶／基数排序

思想：
待排数组成员在有限区间内
构建在区间一次排序的空桶
将每个成员放在对应的桶内
去掉空桶，已排序


for each digit placing

  for each element in list

    move element into respective bucket

  for each bucket, starting from smallest digit

    while bucket is non-empty

      restore element to list

平均时间O(d(r+n)) 最短时间O(d(rd+n)) 最长时间O(d(r+n)) 空间O(rd+n)) 稳定      r基数，d长度
"""