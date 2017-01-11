
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