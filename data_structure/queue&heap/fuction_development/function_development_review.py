from collections import deque
import math


def solution(progresses, speeds):
    answer = []

    queue = deque()
    for i in range(len(progresses)):
        queue.append((progresses[i], speeds[i]))

    now_date = 0
    count = 0
    while queue:
        progress, speed = queue.popleft()
        end_date = int(math.ceil((100-progress)/speed))
        if now_date >= end_date:
            count += 1
        else:
            answer.append(count)
            count = 1
            now_date = end_date
    answer.append(count)
    return answer[1:]


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([1, 95, 95, 95], [99, 1, 1, 1]))
