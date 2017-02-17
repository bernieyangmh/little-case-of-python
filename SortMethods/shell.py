
"""
希尔排序

思想：
先对序列分割，分隔后的数组排序
合并后再进行插入排序
分隔的增量的取值规则最好为第一次取总长度的一半,第二次取一半的一半,依次累推直到1为止。

平均时间O(n**1.3) 最短时间O(n) 最长时间O(n**2) 空间O(1) 不稳定
"""


def shellSort(nums):
    # 间隔长度
    print(nums)
    step = len(nums)//2
    print(step)
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定间隔长度之前的值比较, 符合条件则交换位置
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                print(nums)
                i -= step
        step = step//2
        print(step)
    return nums

nums = [11,17,9,3,5,16,8,2,14,4,0,11,13,7,1]
print(shellSort(nums))