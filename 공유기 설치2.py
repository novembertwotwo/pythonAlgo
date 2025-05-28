import sys

def input():
    return sys.stdin.readline()

N, C = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

def check(arr, interval):
    count = 1
    prev = arr[0]
    for i in range(1, N):
        if arr[i] - prev >= interval:
            count += 1
            prev = arr[i]
            if count == C:
                return True
    return count >= C

start = 1
end = array[-1] - array[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    if check(array, mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)
