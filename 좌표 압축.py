N = int(input())
array = list(map(int,input().split()))
nums = dict()
sortedArray = sorted(set(array))
order = dict()


for i in range(len(sortedArray)):
    order[sortedArray[i]] = i

for i in array:
    print(order[i],end= ' ')




