import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    a,b = input().split()
    array.append((a,int(b)))


array = sorted(array,key = lambda student: student[1])

for student in array:
    print(student[0],end=' ')




