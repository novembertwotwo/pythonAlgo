def gold(n,m,array):
    maxVal = 0
    dp = [[0]* m for _ in range(n)]
    for i in range(n):
        dp[i][0] = array[i][0]
    for y in range(m-1):
        for x in range(n):
            if 0<x<n-1:
                dp[x][y+1] = max(dp[x-1][y],dp[x][y],dp[x+1][y])+array[x][y+1]
            elif x==0:
                dp[x][y + 1] = max( dp[x][y], dp[x + 1][y]) + array[x][y + 1]
            elif x==n-1:
                dp[x][y + 1] = max(dp[x - 1][y], dp[x][y]) + array[x][y + 1]
    for i in range(n):
        maxVal = max(maxVal,dp[i][m-1])
    return maxVal

T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    data = []
    for i in range(0,len(array),m):
        data.append(array[i:i+m])
    print(gold(n,m,data))