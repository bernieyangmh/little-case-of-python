import math


class LazyProperty(object):
    """
    类装饰器
    这个装饰器能帮助我们延迟类属性的计算。一旦访问建立一个实例，计算结果被保存起来
    LazyProperty
    explain: http://www.spiderpy.cn/blog/5/
    """

    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius


c = Circle(2)
b = Circle(4)
print(c.area)
print(c.area)
print(b.perimeter)
print(b.perimeter)
