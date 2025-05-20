import sys
from collections import deque

input =sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
for _ in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1
m = int(input())
q= deque()
for i in range(m):
    a,b=input().split()
    q.append((int(a),b))

count = 0

snake = deque([(0,0)])

dx=[-1,0,1,0]
dy=[0,1,0,-1]
d = 1

while True:
    count += 1
    x,y = snake[-1]
    x += dx[d]
    y += dy[d]
    if x<0 or y<0 or x>=n or y>=n:
        break
    if graph[x][y] == 1:
        snake.append((x,y))
        graph[x][y] = 0
    else:
        if (x,y) in set(snake):
            break
        snake.popleft()
        snake.append((x,y))
    if q and count == q[0][0]:
        if q[0][1] == "D":
            d = (d+1)%4
        else:
            d = (d-1)%4
        q.popleft()

print(count)












