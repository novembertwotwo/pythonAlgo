n = int(input())
array =list(map(int,input().split()))

def binary_search(array,start,end):
    while start<=end:
        mid = (start + end) // 2
        if array[mid]<mid:
            start = mid+1
        elif array[mid]>mid:
            end = mid - 1
        else:
            return mid
    return -1

print(binary_search(array,0,len(array)-1))





