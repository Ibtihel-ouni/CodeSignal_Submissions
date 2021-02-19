from collections import Counter

def firstNotRepeatingCharacter(s):
    c = Counter()
    for i in s:
        c[i] += 1
    for i in s :
        if c[i] == 1:
            return i
    return "_"
