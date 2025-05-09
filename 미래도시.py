import sys

input = sys.stdin.readline
N, M = map(int, input().split())
INF =int(1e9)
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]



for i in range(N):
    for j in range(N):
        if i==j:
            graph[i][j] = 0


for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X,K = map(int, input().split())

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[b][k])
result = graph[1][K] + graph[K][X]
print(result) if result<=INF else print(-1)



