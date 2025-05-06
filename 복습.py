import sys
input =sys.stdin.readline
N = int(input())
array = list(int(input()) for _ in range(N))
now = 1
stack = [now]
result = ["+"]
flag = True

for i in array:
    while i > now:
        now +=1
        stack.append(now)
        result.append("+")
    if stack and i == stack[-1]:
        stack.pop()
        result.append("-")
    elif stack and i<stack[-1]:
        flag = False
        break

if flag:
    print('\n'.join(result))
else:
    print("NO")