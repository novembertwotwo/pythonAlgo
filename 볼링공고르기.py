import sys
input = sys.stdin.readline

N,M = map(int,input().split())

count = 0
array = list(map(int,input().split()))

for i in range(len(array)):
    now = array[i]
    if now > M:
        continue
    for j in array[i+1:]:
        if now!=j and j<=M:
            count +=1
print(count)


