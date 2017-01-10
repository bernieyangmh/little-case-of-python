def max_val(w, v, i, aW):
    print('max_val called with:', i, aW)
    global numCalls
    numCalls += 1
    if i == 0:
        if w[i] <= aW:
            return v[i]
        else:
            return 0
    without_i = max_val(w, v, i-1, aW)
    if w[i] > aW:
        return without_i
    else:
        with_i = v[i] + max_val(w, v, i-1, aW-w[i])
    return max(with_i, without_i)

def max_val0(w, v, i, aW):
    return max_val(w, v, i, aW)

def fast_max_val(w, v, i, aW, m):
    print('max_val called with:', i, aW)
    global numCalls
    numCalls += 1
    try:
        return m[(i, aW)]
    except KeyError:
        if i == 0:
            if w[i] <= aW:
                m[(i, aW)] = v[i]
                return v[i]
            else:
                m[(i, aW)] = 0
                return 0
        without_i = fast_max_val(w, v, i-1, aW, m)
        if w[i] > aW:
            m[(i, aW)] = without_i
            return without_i
        else:
            with_i = v[i] + fast_max_val(w, v, i-1, aW-w[i], m)
            res = max(without_i,with_i)
            m[(i, aW)] = res
            return res


def max_val1(w, v, i, aW):
    m = {}
    return fast_max_val(w, v, i, aW, m)

maxWeight = 40
w=[5,5,1,3,4,2,7,8,9,4,2,4,5,6,7,8,9,3,5,5,4,6,1,2,3,4,5,6,7,4]
v=[6,7,8,4,1,9,1,0,3,4,5,2,1,3,7,8,6,4,4,5,6,9,3,4,5,6,2,3,4,5]
numCalls = 0
res = max_val1(w, v, len(v)-1, maxWeight)
print('fast max val = ', res, 'number of calls =', numCalls)
