import sys
input = sys.stdin.readline
N = int(input())
array = list(map(int,input().split()))
array.reverse()

stack = []
result = []

for num in array:
    if stack and stack[-1]>num:
        result.append(stack[-1])
        stack.append(num)
        continue
    while stack and stack[-1]<=num:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(num)
    stack.append(num)
if len(stack)==1:
    result[-1] = -1

result.reverse()
result[-1]= -1
print(' '.join(map(str,result)))








