# -*- coding: utf-8 -*-

"""
    Draw Line Problem
    The work is done by the recursive draw interval function.
This function draws the sequence of minor ticks within some
interval, based upon the length of the interval’s central tick.
We rely on the intuition shown at the top of this page, and
with a base case when L = 0 that draws nothing.For L ≥ 1, the
first and last steps are performed by recursively calling
draw interval(L − 1).The middle step is performed by calling
the function draw line(L).
"""
x = 0


def draw_line(tick_length, tick_label='.'):
    """Draw one line with given tick length (followed by optional label)."""
    global x
    print(tick_length)
    line = '_' * tick_length
    if tick_label:
        line += '' + tick_label
        print(line)
        x += 1
        print('execute draw_line num is ', x)


def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_rule(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, 't')          # Honestly, this line of code shouldn't execute if we want see the law.
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))   # Honestly, this line of code shouldn't execute if we want see the law.

draw_rule(1, 6)


'''
num of appear
5 - 1
4 - 2
3 - 4
2 - 8
1 - 16
'''

#####################################################

"""There's different function about recursion in 'SeachMethods', is 'binary_search'. """
