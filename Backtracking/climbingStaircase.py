def climbingStaircase(n, k):
    d = {0: [[]]}
    def f(n):
        if n in d:
            return d[n]
        ans = []
        for x in xrange(1, min(n,k) + 1):
            for y in f(n - x):
                ans.append([x] + y)
        d[n] = ans
        return ans
    return f(n)

