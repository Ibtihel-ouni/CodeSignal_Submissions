from collections import Counter

def containsDuplicates(a):
    c = Counter()
    for i in range(len(a)):
        c[a[i]] += 1
        if c[a[i]] > 1 :
            return True
    return False
    
