# -*- coding: utf-8 -*-

"""
3.0版本 izip()———>zip(), izip_longest()--->zip_longest()
"""
from Itertools import *

print('{0:-<10} {1} {2:->10}'.format('-', 'product', '-'))
# 笛卡尔积
eg = product('ABCD', 'xy')
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'combinations', '-'))
# 同元素不可重复，不考虑index
eg = combinations(['a', 'b', 'c'], 2)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'permutations', '-'))
# 返回所有 r个项，iterable中的元素为元素的可能组合，考虑同元素不同index
eg = permutations(['a', 'b', 'c'], 2)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'combinations_with_replacement', '-'))
# 同元素可重复，不考虑index
eg = combinations_with_replacement(['a', 'b', 'c'], 2)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'product', '-'))
# 同元素可重复，考虑index
eg = product('ABC', repeat=2)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'repeat', '-'))
# 重复
eg = repeat('ABC', 2)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'accumulate', '-'))
# 累加
eg = accumulate([1, 2, 3, 4, 5])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'chain', '-'))
# 将多个迭代器作为参数, 返回单个迭代器
eg = chain('abc', 'def')
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'compress', '-'))
# 根据selectors中的数字过滤data
eg = compress('abc', [1, 0, 1])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'cycle', '-'))
# 以iterable为一轮循环重复
_con = 0
eg = []
for i in cycle(['a', 'b', 'c']):
    eg.append(i)
    _con += 1
    if _con > 12:
        break
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'count&zip', '-'))
# 从start开始计数，间隔step
eg = zip(count(1, 2), ['a', 'b', 'c'])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'dropwhile', '-'))


# 保留第一个False之后的值
eg = dropwhile(lambda x: x < 0.5, [-2, -1, 0, 1, 2])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'takewhile', '-'))
# 返回function的结果为False之前的结果（-1 != False)
eg = takewhile(lambda x: x / 1, [-3, 4, -1, 0, 3, 4, 1, -2])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'filterfalse', '-'))
# 根据所给函数过滤
eg = filterfalse(lambda x: x % 2, range(10))
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'groupby', '-'))
# 根据所给函数应用于每个元素的结果分组，无函数则全部分组
eg = ['aa', 'ab', 'ABC', 'bcd', 'ABCD', 123]
for i, k in groupby(eg, type):
    print(i, list(k))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'islice', '-'))
# iterable，起始位置，结束位置，间隔
eg = islice(count(), 0, 100, 10)
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'starmap', '-'))
# 对iterable的每个元素应用function
eg = starmap(pow, [(2, 5), (3, 2), (10, 3)])
print(list(eg))

print('{0:-<10} {1} {2:->10}'.format('\n-', 'tee', '-'))
# 把一个迭代器分为n个迭代器,返回一个元祖
eg = tee(range(10), 4)
print([list(i) for i in list(eg)])

print('{0:-<10} {1} {2:->10}'.format('\n-', 'zip_longest', '-'))
# 类似zip但空缺不会去掉，用fillvalue补足
eg = zip_longest('ABCD', 'xy', fillvalue='?')
print(list(eg))
