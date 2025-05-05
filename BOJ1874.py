import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.reverse()

stack = []
result = []

for num in array:
    while stack and stack[-1] <= num:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)  # 스택이 비면 -1 추가
    stack.append(num)

result.reverse()
print(' '.join(map(str, result)))
