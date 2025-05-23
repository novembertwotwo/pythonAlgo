N = int(input())
array = []
for i in range(N):
    a,b= map(int,input().split())
    array.append((a,b))
array.sort(key = lambda x:(x[1],x[0]))
print(array)
