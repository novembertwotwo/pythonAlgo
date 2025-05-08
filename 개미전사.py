import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = array[0]

for i in range(1, N):
    if i > 1:
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i])
    else:
        dp[i] = max(dp[i-1],array[i])
print(dp[-1])


