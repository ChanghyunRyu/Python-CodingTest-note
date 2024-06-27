from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        progress, speed = progresses[i], speeds[i]
        clear = int(math.ceil((100-progress)/speed))
        q.append(clear)

    before_clear = 0
    count = 0
    while q:
        now_clear = q.popleft()
        if now_clear > before_clear:
            if before_clear != 0:
                answer.append(count)
            count = 1
        else:
            count += 1
        before_clear = max(before_clear, now_clear)
    else:
        answer.append(count)
    return answer


print(solution([90, 98, 97, 96, 98], [1, 1, 1, 1, 1]))
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([95, 95, 95, 95], [4, 3, 2, 1]))
print(solution([1, 95, 95, 95], [99, 1, 1, 1]))
