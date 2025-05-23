S = input()
result = set([])
length =len(S)
for i in range(1,length+1):
    for j in range(length):
        temp = S[j:j+i]
        result.add(temp)
print(len(result))

