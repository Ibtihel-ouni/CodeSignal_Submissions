def areFollowingPatterns(strings, patterns):
    if len(set(strings)) != len(set(patterns)):
        return False
    d = {}
    for i, j in zip(strings, patterns):
        if i in d and d[i] != j:
            return False
        d[i] = j
    return len(d) == len(set(d.values()))
