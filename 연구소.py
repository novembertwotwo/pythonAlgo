from collections import deque
from copy import deepcopy

n, m = map(int, input().split())


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


def dfs(start,count):
    global result
    if count == 3:
        result = max(result,virus(array))
        return
    for i in range(start,n):
        for j in range(m):
            if array[i][j] == 0:
                array[i][j] = 1
                dfs(i,count+1)
                array[i][j] = 0

def check(array):
    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 0:
                count += 1
    return count


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

array = list(list(map(int,input().split())) for _ in range(n))
result = 0


dfs(0,0)
print(result)






