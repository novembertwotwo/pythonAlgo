n = input()

result = 0

onePath = 0
zeroPath = 0

past = int(n[0])
if past==0:
    zeroPath+=1
else:
    onePath+=1


for i in n:
    now = int(i)
    if past != now:
        if now ==1:
            onePath+=1
            past = 1
        else:
            zeroPath+=1
            past = 0
print(min(onePath,zeroPath))