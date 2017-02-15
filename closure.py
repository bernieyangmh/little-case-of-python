"""

保存了外部传来的参数

"""

def make_adder(a):
    print(a)
    def adder(b):
        print(b)
        return b + a
    return adder

p = make_adder(3)       #3是外部函数a
q = make_adder(4)

p(10)       #10是内部函数b
q(10)

