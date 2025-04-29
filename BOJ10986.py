import sys
input =sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int,input().split()))
sumArray = []
now = 0
for i in range(0,N):
    now += array[i]
    sumArray.append(now%M)

countArray = list(0 for _ in range(M))

for i in sumArray:
    countArray[i]+=1
result = 0
for i in countArray:
    if i>1:
        result += (i*(i-1))/2
result += countArray[0]

print(int(result))



