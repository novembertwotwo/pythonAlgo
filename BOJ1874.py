import sys

input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]

stack = []
result = []
current = 1  # 현재 push할 숫자
flag = True

for target in array:
    # target까지 push
    while current <= target:
        stack.append(current)
        result.append("+")
        current += 1

    # pop 가능한 경우
    if stack and stack[-1] == target:
        stack.pop()
        result.append("-")
    else:  # 불가능한 경우
        flag = False
        break

print('\n'.join(result) if flag else "NO")
