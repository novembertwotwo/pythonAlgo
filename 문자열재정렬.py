array = list(input())

result = []
now = 0
for i in array:
    if i.isalpha():
        result.append(i)
    else:
        now += int(i)
result.sort()
result.append(str(now))

print(''.join(result))
