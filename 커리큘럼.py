import copy
import sys
from collections import deque

input =sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
degree = [0] *(N+1)

cost = [0] * (N+1)


for i in range(1,N+1):
    temp = list(map(int,input().split()))
    cost[i] = temp[0]
    for j in temp[1:-1]:
        graph[j].append(i)
        degree[i] += 1


result = copy.deepcopy(cost)
q= deque()
for i in range(1,N+1):
    if degree[i] == 0:
        q.append(i)
while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i],result[now] + cost[i])
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

for i in result[1:]:
    print(i,end='\n')














