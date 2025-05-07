N,M = map(int,input().split())
array = list(map(int,input().split()))

start = 1
end = max(array)
result = 0

while start<=end :
    mid = (start+end)//2
    sum = 0
    for i in array:
        if i>mid:
            sum += (i%mid)
    if sum >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)









