import sys
import heapq

input = sys.stdin.readline
N = int(input())
minHeap = []
result = []

for _ in range(N):
    temp = int(input())
    if temp==0:
        if not minHeap:
            result.append('0')
        else:
            result.append(str(heapq.heappop(minHeap)))
    else:
        heapq.heappush(minHeap,temp)
        
print('\n'.join(result))


