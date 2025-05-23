from collections import deque

N,K = map(int,input().split())
array = list(list(map(int,input().split())) for _ in range(N))

S,X,Y = map(int,input().split())

dx =[-1,1,0,0]
dy=[0,0,1,-1]

q = []
for i in range(N):
    for j in range(N):
        if array[i][j] != 0:
            q.append((array[i][j],i,j))
q.sort()
q= deque(q)

total_count = len(q)
count = 0
while q and S:
    now,x,y = q.popleft()
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if 0<= nx< N and 0<=ny<N and array[nx][ny]==0:
            q.append((now,nx,ny))
            array[nx][ny] = now
    count +=1
    if count == total_count:
        count = 0
        total_count = len(q)
        S-=1
print(array[X-1][Y-1])









