from tenacity import retry

n = int(input())
array = list(map(int,input().split()))
array.sort()
length = len(array)
if length%2==0 and length>1:
    print(array[length//2 - 1])
else:
    print(array[length//2])

