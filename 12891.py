import sys

def check():
    global result
    if aC >= A and cC >= C and gC >= G and tC >= T:
        result += 1


input = sys.stdin.readline
N, M = map(int, input().split())
array = list(input().strip())
A, C, G, T = map(int, input().split())


result = 0
aC = cC = gC = tC = 0

for i in range(M):
    if array[i] == 'A': aC +=1
    elif array[i] == 'C': cC +=1
    elif array[i] == 'G': gC +=1
    elif array[i] == 'T': tC +=1

check()

for i in range(M, N):
    # 제거될 왼쪽 문자
    left = array[i - M]
    if left == 'A':
        aC -= 1
    elif left == 'C':
        cC -= 1
    elif left == 'G':
        gC -= 1
    elif left == 'T':
        tC -= 1

    # 추가될 오른쪽 문자
    right = array[i]
    if right == 'A':
        aC += 1
    elif right == 'C':
        cC += 1
    elif right == 'G':
        gC += 1
    elif right == 'T':
        tC += 1

    check()

print(result)

