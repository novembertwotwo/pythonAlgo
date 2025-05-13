# import sys
# input =sys.stdin.readline
array = input()
result = 0

for i in array:
    num = int(i)
    if num<=1 or result<=1:
        result += num
    else:
        result *=num
print(result)
