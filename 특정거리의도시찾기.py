import sys
from collections import deque

input = sys.stdin.readline
N,M,K,X = map(int,input().split())
INF =int(1e9)
graph=[[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

q = deque([(0,X)])
distance[X] = 0

while q:
    cost,now = q.popleft()
    for i in graph[now]:
        if cost+1 < distance[i]:
            distance[i] = cost+1
            q.append((cost+1,i))

result = []
for i in range(1,N+1):
    if distance[i] == K:
        result.append(i)
if not result:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)













