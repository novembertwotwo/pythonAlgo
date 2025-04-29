import sys
input = sys.stdin.readline
N,M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]
sumArray = []

for i in range(N):
    temp = [0]
    for j in range(N):
        temp.append(temp[j]+array[i][j])
    sumArray.append(temp)


for _ in range(M):
    a,b,c,d = map(int,input().split())
    result = 0
    for i in range(a-1,c):
        result += sumArray[i][d] - sumArray[i][b-1]
    print(result)












