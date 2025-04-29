n = int(input())
array = list(map(int, input().split()))
maxValue = max(array)
sum = 0
for i in array:
    sum += (i/maxValue) * 100

print(sum/ len(array))
