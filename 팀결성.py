import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] !=x :
        find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



N,M = map(int,input().split())

parent = [x for x in range(N+1)]



result = []

for _ in range(M):
    a,b,c = map(int,input().split())
    if a==0:
        union_parent(parent,b,c)
    else:
        if find_parent(parent,b)==find_parent(parent,c):
            result.append("YES")
        else:
            result.append("NO")

print("\n".join(result))



