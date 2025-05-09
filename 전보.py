import heapq
import sys

input = sys.stdin.readline
N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]
INF = int(1e9)
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for target, cost in graph[now]:
            if distance[target]>cost+ dist:
                heapq.heappush(q,(cost+dist,target))
                distance[target] = cost+dist
dijkstra(C)

count = 0
time = 0
distance[C] = INF
for i in distance:
    if i != INF:
        count+=1
        time = max(time,i)
print(count,time)

