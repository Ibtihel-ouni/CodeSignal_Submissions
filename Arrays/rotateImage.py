def rotateImage(a):
    N = len(a[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = a[i][j]
            a[j][N - 1 - i],a[i][j],a[N - 1 - j][i], a[N - 1 - i][N - 1 - j] = a[i][j] ,a[N - 1 - j][i],a[N - 1 - i][N - 1 - j] , a[j][N - 1 - i]
            
    return a

