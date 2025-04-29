import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
array = map(int, input().split())
array = sorted(array)

start = array[0]
end = array[-1]

startIndex = 0
endIndex = N-1
result = 0
while startIndex < endIndex:
    if start + end < M:
        startIndex += 1
        start = array[startIndex]
    elif start + end > M:
        endIndex -= 1
        end = array[endIndex]
    else:
        startIndex += 1
        endIndex -= 1
        start = array[startIndex]
        end = array[endIndex]
        result += 1
    print(startIndex,endIndex)
    print(result)

print(result)
