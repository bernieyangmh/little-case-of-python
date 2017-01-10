def max_val(w, v, i, aw):
    print('max_val called with:', i, aw)
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aw:
            return v[i]
        else:
            return 0
    without_i = max_val(w, v, i - 1, aw)
    if w[i] > aw:
        return without_i
    else:
        with_i = v[i] + max_val(w, v, i - 1, aw - w[i])
    return max(with_i, without_i)


def max_val0(w, v, i, aw):
    return max_val(w, v, i, aw)


def fast_max_val(w, v, i, aw, m):
    """
    An efficient method of computing the Knapsack Problem by "space for time"
    we remember the computed record in a dict.
    """
    print('max_val called with:', i, aw)
    global numCalls
    numCalls += 1
    try:
        return m[(i, aw)]
    except KeyError:
        if i == 0:
            if w[i] <= aw:
                m[(i, aw)] = v[i]
                return v[i]
            else:
                m[(i, aw)] = 0
                return 0
        without_i = fast_max_val(w, v, i - 1, aw, m)
        if w[i] > aw:
            m[(i, aw)] = without_i
            return without_i
        else:
            with_i = v[i] + fast_max_val(w, v, i - 1, aw - w[i], m)
            res = max(without_i, with_i)
            m[(i, aw)] = res
            return res


def max_val1(w, v, i, aw):
    m = {}
    return fast_max_val(w, v, i, aw, m)


maxWeight = 40
w = [5, 5, 1, 3, 4, 2, 7, 8, 9, 4, 2, 4, 5, 6, 7, 8, 9, 3, 5, 5, 4, 6, 1, 2, 3, 4, 5, 6, 7, 4]
v = [6, 7, 8, 4, 1, 9, 1, 0, 3, 4, 5, 2, 1, 3, 7, 8, 6, 4, 4, 5, 6, 9, 3, 4, 5, 6, 2, 3, 4, 5]
numCalls = 0
res = max_val0(w, v, len(v) - 1, maxWeight)
print('fast max val = ', res, 'number of calls =', numCalls)
