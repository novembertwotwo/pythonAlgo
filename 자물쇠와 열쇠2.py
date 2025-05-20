def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def check(a):
    n = len(a) // 3
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if a[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    array = [[0] * (3 * n) for _ in range(3 * n)]

    for i in range(n):
        for j in range(n):
            array[n + i][n + j] = lock[i][j]

    for k in range(4):
        key = rotate(key)
        for x in range(0, 2 * n):
            for y in range(0, 2 * n):
                for i in range(m):
                    for j in range(m):
                        array[x + i][y + j] += key[i][j]
                if check(array):
                    return True
                for i in range(m):
                    for j in range(m):
                        array[x + i][y + j] -= key[i][j]
    return False
