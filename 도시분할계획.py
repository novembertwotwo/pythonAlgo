import heapq
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())

parent = [x for x in range(N + 1)]

q = []

for _ in range(M):
    a, b, distance = map(int, input().split())
    heapq.heappush(q, (distance, a, b))

result = 0
last = 0
while q:
    distance, a, b = heapq.heappop(q)
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a, b)
        result += distance
        last = distance

print(result-last)