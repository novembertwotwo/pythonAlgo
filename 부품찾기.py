import sys

input = sys.stdin.readline
N = int(input())
store = set(map(int, input().split(" ")))
M = int(input())
need = list(map(int, input().split(" ")))

for i in need:
    if i in store:
        print('yes', end=' ')
    else:
        print('no', end=' ')

