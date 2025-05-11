N = int(input())
arr = list(map(int, input().split()))

arr.sort()


result = 0
cnt = 0

for i in range(N):
    cnt += 1
    print(cnt,arr)
    if cnt >= arr[i]:
        result += 1
        cnt = 0

print(result)