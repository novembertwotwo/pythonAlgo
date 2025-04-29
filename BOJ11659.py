import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
sumArray = [0]
for num in range(1, N+1):
    sumArray.append(sumArray[num-1] + array[num-1])
for _ in range(M):
    a, b = map(int, input().split())
    print(sumArray[b] - sumArray[a-1])
