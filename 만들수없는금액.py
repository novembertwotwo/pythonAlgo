import sys
input = sys.stdin.readline

N = int(input())
graph = list(map(int,input().split()))
graph.sort()

target = 1
for i in graph:
    if target<i:
        break
    target += i

print(target)

