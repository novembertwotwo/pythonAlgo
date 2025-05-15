array = list(input())

a = 0
b = 0
for i in range(len(array)//2):
    a += int(array[i])
for i in range(len(array)//2,len(array)):
    b += int(array[i])
print("LUCKY") if a==b else print("READY")
