import sys

def binary_search(array,target,start,end):
    while start<=end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return False



input = sys.stdin.readline
N = int(input())
store = list(map(int, input().split(" ")))
M = int(input())
need = list(map(int, input().split(" ")))
store.sort()

for i in need:
    result = binary_search(store,i,0,N-1)
    if result:
        print('yes',end=' ')
    else:
        print('no', end=' ')

