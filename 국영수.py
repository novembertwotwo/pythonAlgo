N = int(input())
array = []
for i in range(N):
    a,b,c,d = input().split()
    array.append((a,int(b),int(c),int(d)))
array.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(array[i][0])