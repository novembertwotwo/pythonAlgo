import sys

input = sys.stdin.readline
N = int(input())
array = list(map(int, input().split()))
array.reverse()

stack = []
result = []

for i in array:
    if stack:
        if stack[-1] > i:
            result.append(stack[-1])
            stack.append(i)
        else:
            while stack and stack[-1] <= i:
                stack.pop()
            if stack:
                result.append(stack[-1])
                stack.append(i)
    if not stack:
        stack.append(i)
        result.append(-1)
result.reverse()
print(' '.join(map(str,result)))
