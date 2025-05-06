from collections import deque

N, M = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(N))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0 , 1)])

while queue:
    x, y ,now = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = now+1
                queue.append((nx,ny,graph[nx][ny]))
            elif  graph[nx][ny]>now + 1:
                graph[nx][ny] = now +1
                queue.append((nx, ny, graph[nx][ny]))
print(graph)





