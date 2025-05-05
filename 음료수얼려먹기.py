N, M = map(int, input().split(" "))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = list(list(map(int, input())) for _ in range(N))


def dfs(x, y):
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny< M and not graph[nx][ny]:
            dfs(nx, ny)

result = 0

for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            dfs(i, j)
            result += 1
print(result)
