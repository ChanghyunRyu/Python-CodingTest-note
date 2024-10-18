from collections import deque
import math


def solution(progresses, speeds):
    q = deque()
    answer = []
    for i in range(len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        q.append(day)
    print(q)
    while q:
        now_job = q.popleft()
        count = 1
        while q and q[0] <= now_job:
            q.popleft()
            count += 1
        answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([1, 95, 95, 95], [99, 1, 1, 1]))
print(solution([96, 94],[3, 3]))
