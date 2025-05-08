N, M = map(int, input().split())
array=[int(input()) for _ in range(N)]
dp= [0]*(M+1)

for i in array:
    if i<=M:
        dp[i] += 1


for i in range(M+1):
    for j in array:
        if dp[i] and i+j<=M:
            if dp[i+j]:
                dp[i+j] = min(dp[i+j],dp[i] + 1)
            else:
                dp[i+j]= dp[i] + 1


print(dp[-1]) if dp[-1] else print(-1)








