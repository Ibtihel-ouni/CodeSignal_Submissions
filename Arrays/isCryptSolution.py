def isCryptSolution(crypt, solution):
    hasLeadingZeros = False
    # a + b = c
    a = crypt[0]
    b = crypt[1]
    c = crypt[2]
    
    d = {}
    
    for s in solution:
        d[s[0]] = int(s[1])
        
    if d[a[0]] == 0 or d[b[0]] == 0 or d[c[0]] == 0:
        hasLeadingZeros = True

        
    n1 = ''.join([str(d[i]) for i in a])
    n2 = ''.join([str(d[i]) for i in b])
    n3 = ''.join([str(d[i]) for i in c])
    
    if int(n1) + int(n2) == int(n3):
        if hasLeadingZeros and int(n3) == 0 and len(n3) == len(str(int(n3))):
            return True
        elif hasLeadingZeros:
            return False
        else:
            return True
    else:
        return False
