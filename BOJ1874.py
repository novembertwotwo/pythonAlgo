import sys
input = sys.stdin.readline

N = int(input())
array = list(int(input()) for _ in range(N))

result = []
stack = []
now = 1
flag = True

for target in array:
    while target >= now:
        stack.append(now)
        result.append("+")
        now+=1
    if stack and stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
print('\n'.join(result) if flag else "NO")

