import copy
import heapq
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
array = []
q = []
for _ in range(N):
    n = int(input())
    heapq.heappush(q, n)
    array.append(n)


def check(q, interval):
    count = 1
    start = heapq.heappop(q)
    while q:
        now = heapq.heappop(q)
        if start + interval <= now:
            count += 1
            start = now
        if count == C:
            return True
    return False

array.sort()
start = 1
end = array[-1] - array[0]
flag = False
answer = 1
while start <= end:

    mid = (start + end) // 2
    if check(copy.deepcopy(q), mid):
        start = mid + 1
        answer = max(answer, mid)
    else:
        end = mid - 1

print(answer)
