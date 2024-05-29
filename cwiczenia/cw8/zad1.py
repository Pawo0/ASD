def lis(A,t):
    F = [[False for _ in range(t)] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(t):
            F[i][j] = F[i-A[i]][i-1] or F[i][i-1]
    return F[t][len(A)-1]