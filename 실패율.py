def solution(N, stages):
    now = [0] * (max(stages)+1)
    fail = []
    for i in stages:
        now[i] += 1
    person = len(stages)
    for i in range(1,N+1):
        if person == 0 :
            fail.append((0,i))
            continue
        fail.append((now[i]/person,i))
        person -= now[i]
    fail.sort(key = lambda x: (-x[0],x[1]))
    answer = []
    for i in fail:
        answer.append(i[1])
    return answer