N, M = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(N))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def dfs(x, y, now):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx==0 and ny==0:
            continue
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = now + 1
                dfs(nx, ny, now + 1)
            elif graph[nx][ny] >= now + 1:
                graph[nx][ny] = now + 1
                dfs(nx, ny, now + 1)



dfs(0, 0, 1)
print(graph)
print(graph[N - 1][M - 1])
