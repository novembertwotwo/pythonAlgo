import sys
input = sys.stdin.readline

N = int(input())
array = [[0]*N for _ in range(N)]
dp = [[0]*N for _ in range(N)]
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(len(temp)):
        array[i][j] = temp[j]

dp[0][0] = array[0][0]

for i in range(1,N):
    for j in range(i+1):
        if j==0:
            dp[i][j] = dp[i-1][j] + array[i][j]
        elif j==i:
            dp[i][j] = dp[i-1][j-1] + array[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + array[i][j]
maxVal = 0
for i in range(N):
    maxVal = max(maxVal,dp[N-1][i])

print(maxVal)


