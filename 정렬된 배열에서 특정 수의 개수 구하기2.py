N,M = map(int,input().split())
array = list(map(int,input().split()))

def binary_search_left(start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if (mid==0 or M>array[mid-1]) and array[mid]== M:
        return mid
    elif array[mid]==M:
        return binary_search_left(0,mid-1)
    else:
        return binary_search_left(mid+1,end)

def binary_search_right(start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == N-1 or M < array[mid+1]) and  array[mid] == M:
        return mid
    elif array[mid]==M:
        return binary_search_right(mid+1,N)
    else:
        return binary_search_right(start,mid-1)

def solution():
    left = binary_search_left(0,N-1)
    if left is None:
        return -1
    right = binary_search_right(0,N-1)
    return right-left+1



print(solution())


















