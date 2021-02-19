from collections import Counter

def firstDuplicate(a):
    c = Counter()
    for i in a:
        c[i] += 1
        if c[i] > 1:
            return i

    return -1
