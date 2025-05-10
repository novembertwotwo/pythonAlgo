import heapq

N,M = map(int,input().split())

q=[]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    a,b,distance = map(int,input().split())
    heapq.heappush(q,(distance,a,b))

parent =  [x for x in range(N+1)]

result = 0

while q:
    distance,a,b = heapq.heappop(q)
    if find_parent(parent,a) == find_parent(parent, b):
        continue
    else:
        result += distance
        union_parent(parent, a, b)

print(result)




