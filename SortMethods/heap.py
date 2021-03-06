"""
堆排序

思想：
构建堆
输出堆顶
堆底元素与堆顶交换，在检查堆
1.根结点与左、右子树中较小元素的进行交换
2.与左子树交换：如果左子树堆被破坏，递归1
3.若与右子树交换，如果右子树堆被破坏，递归1
对子叶重复1，2，3

平均时间O(Nlog2N) 最短时间O(Nlog2N) 最长时间O(Nlog2N) 空间O(1) 不稳定
"""