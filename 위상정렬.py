from collections import deque

N, M = map(int, input().split())

array = [[] for _ in range(N + 1)]
count = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    count[b] += 1
    array[a].append(b)

q = deque()
for i in range(1, N + 1):
    if count[i] == 0:
        q.append(i)

result = []

while q:
    print(q)
    now = q.popleft()
    result.append(now)
    for i in array[now]:
        count[i] -= 1
        if count[i] == 0:
            q.append(i)

print(result)
