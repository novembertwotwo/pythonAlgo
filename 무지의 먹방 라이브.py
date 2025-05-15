from collections import deque


def solution(food_times, k):
    q = deque()
    for i in range(len(food_times)):
         q.append((i+1,food_times[i]))
    while q and k:
        now,a = q.popleft()
        a-=1
        if a!=0:
            q.append((now,a))
        k-=1

    if q:
        return q.popleft()[0]
    else:
        return -1


print(solution([10,11,2],5))
