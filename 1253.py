import sys


input = sys.stdin.readline
N = input()
array = list(map(int, input().split()))
array.sort()

start = array[0]
end = array[-1]
startIndex = 0
endIndex = N - 1
result = 0
count = 0

while startIndex < endIndex:
    if start +end < N :
        startIndex += 1
        start = array[startIndex]
    elif start+end >N:
        endIndex-=1
        end = array[endIndex]
    else:
        startIndex+=1
        endIndex-=1
        start=array[startIndex]
        end =array[endIndex]
        result += 2

print(result)


