from collections import deque
from copy import deepcopy

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

array = [list(map(int, input().split())) for _ in range(n)]
result = 0

empty = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            empty.append((i, j))

def virus(array):
    temp = deepcopy(array)
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 2:
                q = deque([(x, y)])
                while q:
                    a, b = q.popleft()
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                            temp[nx][ny] = 2
                            q.append((nx, ny))
    return check(temp)

def check(array):
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count += 1
    return count

def dfs(start, count):
    global result
    if count == 3:
        result = max(result, virus(array))
        return
    for idx in range(start, len(empty)):
        i, j = empty[idx]
        array[i][j] = 1
        dfs(idx + 1, count + 1)
        array[i][j] = 0

dfs(0, 0)
print(result)
