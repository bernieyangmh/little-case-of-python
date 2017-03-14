import time

"""
mro与super
新式类object 采用c3广度优先的继承
"""
class A(object):

    def __init__(self):
        print('enter a')
        self.name='a class'
        self.time =time.ctime()
        time.sleep(1)

class B(A):

    def __init__(self):
        print('enter b')
        super(B, self).__init__()

class C(A):

    def __init__(self):
        print('enter c')
        super(C, self).__init__()

class D(A):
    def __init__(self):
        print('enter d')
        super(D, self).__init__()

class E(B,C):
    def __init__(self):
        print('enter e')
        super(E, self).__init__()

class F(C,D):
    def __init__(self):
        print('enter f')
        super(F, self).__init__()

class G(E,F):
    def __init__(self):
        print('enter g')
        super(G, self).__init__()

g=G()
print(g.name)
print(g.time)
print(G.__mro__)

"""
        A
       /|\
      / | \
     /  |  \
    B   C   D
     \ / \ /
      E   F
       \ /
        G
"""