def check():
    flag = True
    for i in range(4):
        if needCount[i]>nowCount[i]:
            flag = False
    return flag

S,P = map(int,input().split())

array = list(input())
needCount = list(map(int,input().split()))

result = 0
nowCount = [0, 0, 0, 0]

for i in range(0,P):
    if array[i] == 'A':
        nowCount[0] +=1
    elif array[i] == 'C':
        nowCount[1] += 1
    elif array[i] == 'G':
        nowCount[2] += 1
    elif array[i] == 'T':
        nowCount[3] += 1

for i in range(0,S-P+1):
    if i>0:
        if array[i-1] == 'A':
            nowCount[0] -= 1
        elif array[i-1] == 'C':
            nowCount[1] -= 1
        elif array[i-1] == 'G':
            nowCount[2] -= 1
        elif array[i-1] == 'T':
            nowCount[3] -= 1
        if array[i+P-1] == 'A':
            nowCount[0] +=1
        elif array[i+P-1] == 'C':
            nowCount[1] += 1
        elif array[i+P-1] == 'G':
            nowCount[2] += 1
        elif array[i+P-1] == 'T':
            nowCount[3] += 1
    if check():
        result +=1
print(result)
