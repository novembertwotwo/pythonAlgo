import heapq
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
INF = int(1e9)
start = int(input())

array=[[] for _ in range(M)]
distance = [INF] * (N+1)

for i in range(M):
    a,b,c = map(int,input().split())
    array[a].append((b,c))


def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in array[now]:
            target = i[0]
            cost = i[1]
            if distance[target]> dist + cost:
                distance[target] = dist + cost
                heapq.heappush(q,(distance[target],target))

dijkstra(1)

print(distance)



