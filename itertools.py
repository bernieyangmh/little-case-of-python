# -*- coding: utf-8 -*-
from itertools import *

# 笛卡尔积
eg = product('ABCD', 'xy')
print(list(eg))

# 同元素不可重复，不考虑index
eg = combinations(['a', 'b', 'c'], 2)
print(list(eg))

# 返回所有 r个项，iterable中的元素为元素的可能组合，考虑同元素不同index
eg = permutations(['a', 'b', 'c'], 2)
print(list(eg))

# 同元素可重复，不考虑index
eg = combinations_with_replacement(['a', 'b', 'c'], 2)
print(list(eg))

# 同元素可重复，考虑index
eg = product('ABC', repeat=2)
print(list(eg))

eg = repeat('ABC', 2)
print(list(eg))

# 累加
eg = accumulate([1, 2, 3, 4, 5])
print(list(eg))

# 将多个迭代器作为参数, 返回单个迭代器
eg = chain('abc', 'def')
print(list(eg))

# 根据selectors中的数字过滤data
eg = compress('abc', [1, 0, 1])
print(list(eg))

# 以iterable为一轮循环重复
_con = 0
eg = []
for i in cycle(['a', 'b', 'c']):
    eg.append(i)
    _con += 1
    if _con > 12:
        break
print(list(eg))

# 从start开始计数，间隔step
eg = zip(count(1, 2), ['a', 'b', 'c'])
print(list(eg))

# 保留第一个False之后的值
def should_drop(x):
    return (x < 0)

eg = dropwhile(should_drop, [-2, -1, 0, 1, 2])
print(list(eg))

# 根据所给函数过滤
eg = filterfalse(lambda x: x%2, range(10))
print(list(eg))

# 根据所给函数应用于每个元素的结果分组，无函数则全部分组
eg = ['aa', 'ab', 'ABC', 'bcd', 'ABCD', 123]
for i, k in groupby(eg, type):
    print(i, list(k))

# iterable，起始位置，结束位置，间隔
eg = islice(count(), 0, 100, 10)
print(list(eg))

# 对iterable的每个元素应用function
eg = starmap(pow, [(2,5), (3,2), (10,3)])
print(list(eg))

# 返回function的结果为False之前的结果（-1 != False)
eg = takewhile(lambda x: x/1, [-3, 4, -1, 0, 3, 4, 1, -2])
print(list(eg))
