import sys
input = sys.stdin.readline

N = int(input())
result = 0

start = 0
end = 0
startIndex = 0
endIndex = 0

while startIndex <= N:
    if end - start < N:
        endIndex += 1
        end += endIndex
    elif end - start > N:
        startIndex += 1
        start += startIndex
    else:
        result += 1
        endIndex += 1
        startIndex += 1
        end += endIndex
        start += startIndex

print(result)




















