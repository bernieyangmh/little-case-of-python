# -*- coding: utf-8 -*-

import ctypes


"""
An illustration of the three steps for “growing” a dynamic array:
    (a) create new array B;
    (b) store elements of A in B;
    (c) reassign reference A to the new array.
"""


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""
    def __init__(self):
        """Create an empty array."""
        self._n = 0                                     # count actual elements
        self._capacity = 1                              # default array capacity
        self._A = self._make_array(self._capacity)      # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]                               # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c."""
        B = self._make_array(c)                         # new (bigger) array
        for k in range(self._n):                        # for each existing value
            B[k] = self._A[k]
        self._A = B                                     # use the bigger array
        self._capacity = c

    def _make_array(self, c):
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()

    def remove(self, value):
        """Remove first occurrence of value (or raise ValueError)"""
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):         # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None             # help garbage collection
                self._n -= 1
                return
        raise ValueError('value not found')

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:                   # not enough room
            self._resize(2 * self._capacity)            # so double capacity
        for j in range(self._n, k, -1):                 # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                              # store newest element
        self._n += 1





DynamicArray_summary = """
    Let us assume that one cyber-dollar is enough to pay for the execution of each append operation in S, excluding
the time spent for growing the array. Also, let us assume that growing the array from size k to size 2k requires k
cyber-dollars for the time spent initializing the new array. We shall charge each append operation three cyber-dollars.
Thus, we overcharge each append operation that does not cause an overflow by two cyber-dollars. Think of the two
cyber-dollars profited in an insertion that does not grow the array as being “stored” with the cell in which the element
was inserted. An overflow occurs when the array S has 2i elements, for some integer i ≥ 0, and the size of the array
used by the array representing S is 2i. Thus, doubling the size of the array will require 2i cyber-dollars. Fortunately,
these cyber-dollars can be found stored in cells 2i−1 through 2i − 1. (See Figure 5.14.) Note that the previous overflow
occurred when the number of elements became larger than 2i−1 for the first time, and thus the cyber-dollars stored in
cells 2i−1 through 2i − 1 have not yet been spent. Therefore, we have a valid amortization scheme in which each
operation is charged three cyber-dollars and all the computing time is paid for. That is, we can pay for the execution
of n append operations using 3n cyber-dollars. In other words, the amortized running time of each append operation is
O(1); hence, the total running time of n append operations is O(n).
"""


#####################################

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack"""
        return len((self._data))

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of stack"""
        self._data.append(e)

    def top(self):
        """Return the element at the top of the stack"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data[-1]

    def pop(self):
        """Return and remove the element from the top of the stack"""
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self._data.pop()

def is_match(expr):
    """
    Return True if all delimiters are properly matchl;False otherwise
    """
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()

eg = '[(5+x)-(y+z)]'
is_match(eg)


#####################################

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue"""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __str__(self):
        """Return data"""
        return str(self._data)

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty"""
        return self._size == 0

    def first(self):
        """Return the element at the front of the queue."""
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue"""
        if self.is_empty():
            raise ValueError('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)                    # % not //
        self._front = 0



    #TODO dequeue后 前面的None还在，占用空间


q = ArrayQueue()
print(q)
q.enqueue('123')
print(q)
q.enqueue('456')
print(q)
q.enqueue('234')
print(q)
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
q.enqueue('453')
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)


#####################################

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    class Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
        self._tail = None

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True if the stack is empty"""
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return the element at the top of the stack."""
        if self.is_empty():
            raise ValueError('LinkedStack is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the element from the top of the stack """
        if self.is_empty():
            raise ValueError('LinkedStack')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """ Add an element to the back of queue.
            The newest node always becomes the new tail.
        """
        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

l = LinkedStack()
l.enqueue('123')
print(l.top())

#####################################

class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next


    def __init__(self):
        """Create an empty queue"""
        self._tail = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise ValueError('Queue is empty')
        head =self._tail._next
        return head._element

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size

    def dequeue(self):
        """Remove and return the first element of the queue """
        if self.is_empty():
            raise ValueError('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next                 # new node points to head       新的节点指向头
            self._tail._next = newest                       # old tail points to new node   老的尾指向新节点
        self._tail = newest                                 # new node becomes the tail     尾指针指向节点
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next

#####################################

class DoublyLinkedBase:
    """
        A base class providing a doubly linked list representation.
        Doubly Linked list allow a greater variety of O(1)-time update operations, including insertions and deletions at
    arbitrary positions within the list.
    """

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                      # trailer is after header
        self._trailer._prev = self._header                      # header is before trailer
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)          # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                                 # record deleted element
        node._prev = node._next = node._element = None           # setting Node fields to None is advantageous as it may
        return element                                          # help Python’s garbage collection


class LinkedQeque(DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return the element at the front of the deque."""
        if self.is_empty():
            raise ValueError('Qeque is empty')
        return self.header.next._element

    def last(self):
        """Return the element at the front of the deque."""
        if self.is_empty():
            raise ValueError('Qeque is empty')
        return self._trailer._prev._element

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque."""
        if self.is_empty():
            raise ValueError('Qeque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque."""
        if self.is_empty():
            raise ValueError('Qeque is empty')
        return self._delete_node(self._trailer._prev)


class PositionalList(DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)

    def _validate(self, p):
        """Return position s node, or raise appropriate error if invalid."""
        print('self.Position is ', type(self.Position))
        print("p's type is ", type(p))
        if not isinstance(p, self.Position):                                                # TODO WHY?
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:                                                           # TODO WHY?
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list"""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """Return the Position just before Position p """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Position just after Position p"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e."""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

def insertion_sort(l):
    """ Sort PositionalList of comparable elements into nondecreasing order.
       we develop an implementation that operates on a PositionalList, relying on the insertion-sort algorithm in which
     each element is placed relative to a growing collection of previously sorted elements.
    """
    if len(l) > 1:
        marker = l.first()
        while marker != l.last():
            pivot = l.after(marker)
            value = pivot.element()
            print('value is ', value)
            if value > marker.element():
                marker = pivot                                                  # 交换位置
            else:
                walk = marker
                while walk != l.first() and l.before(walk).element() > value:
                    walk = l.before(walk)
                l.delete(pivot)
                l.add_before(walk, value)
    else:
        question = 'Why you want use insertion_sort()??'
        print(question)
        return question


l = PositionalList()
print()
l.add_last('9')
l.add_first('0')
l.add_first('1')
# l.add_after(l.Position, '567')  # TODO This have a problem

print(len(l))
print(l._header._next._element)
print(l._header._next._prev._next)



"""e use a general object-oriented design pattern, the composition pattern, in which we define a single object that is composed of two or more other objects. Specifically, we define a nonpublic nested class, Item, that stores the element and its access count as a single instance."""

class FavoriteList:
    """List of elements ordered from most frequently accessed to least."""

    class _item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        """Search for element e and return its Position."""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and
                       cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self.__data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)
        if p is None:
            p =self._data.add_last(self._item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)


class FavoritesListMTF(FavoriteList):
    """List of elements ordered with move-to-front heuristic."""

    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')

        # we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value
            temp.delete(highPos)



class Tree:
    """Base Tree"""

    class Position:

        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not(self == other)

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """返回该结点的深度"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height_slow(self, p):
        return max(self.depth(p) for p in self.position() if self.is_leaf(p))       # 嵌套循环

    def _height_fast(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height_fast(c) for c in self.children(p))          # 递归

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height_fast(p)

class BinaryTree(Tree):
    """
        A binary tree is an ordered tree with the following properties:
    1. Every node has at most two children.
    2. Each child node is labeled as being either a left child or a right child.
    3. A left child precedes a right child in the order of children of a node.
    """
    def left(self, p):
        """Return left child"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return right child"""
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self.__left = left
            self._right = right

    class Position(BinaryTree.Position):

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self.__size = 0

    def __len__(self):                                                      # O(1)
        return self._size

    # O(1) Methods
    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node =self._validate(p)
        old =node._element
        node._element = e
        return old

    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element

    def _attch(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def perorder(self):
        """前序遍历 根左右"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other


    def postorder(self):
        """后序遍历 左右根"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def inorder(self):
        """中序遍历 左根右"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def breadthfirst(self):
        """广度遍历"""
        if not self.is_empty():
            fringe = LinkedQeque()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

    def positions(self):
        return self.inorder()

def parenthetic(T, p):
    """Print parenthesized representation of subtree of T rooted at p."""
    print(p.element(), end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = '('if first_time else  ','
            print(sep, end='')
            first_time = False
            parenthetic(T, c)
        print(')', end='')

"""
    The template method pattern describes a generic computation mechanism that can be specialized for a particular
application by redefining certain steps. To allow customization, the primary algorithm calls auxiliary functions known
as hooks at designated steps of the process.
"""

class EulerTour:
    def __init__(self, tree):
        self._tree =tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        path list of indices of children on path from root to p
        :param p:       Position of current node being visited
        :param d:       depth of p in the tree
        :param path:    path list of indices of children on path from root to p
        :return:
        """
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.childer(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_previsit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*'' + str(p.element))


class PreorderPrintIndententedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j + 1) for j in path)
        print(2*d*'' + label, p.element())


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(',', end='')
        print(p.element(), end='')
        if not self.tree().is_leaf(p):
            print('(', end='')

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(')', end='')

class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree"""

    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

class ExpressionTree(LinkedBinaryTree):
    """for display"""

    def __init__(self, token, left=None, right=None):
        super().__init()
        if not isinstance(token, str):
            raise TypeError('TOKEN MUST BE A STRING')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('token must be a valid operator')
            self._attch(self.root(), left, right)

    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(')')

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())

        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val


def build_expression_tree(tokens):
    """
    Returns an ExpressionTree based upon by a tokenized expression.
    算术表达式转化为树
    """
    S=[]
    for t in tokens:
        if t in '+-x*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
        return S.pop()


#######################################################

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    class _ltem:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)




    def is_empty(self):
        return len(self._data) == 0

class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a sorted list."""
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key"""
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap.
        add & remove_min both are O(logN)
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def _parent(self, j):
        return (j-1)//2

    def _left(self, j):
        return 2*j+1

    def _right(self, j):
        return 2*j+2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._left(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _uphead(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._uphead(parent)
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def add(self, key, value):
        self._data.append(self._item(key, value))
        self._uphead(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)


    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

