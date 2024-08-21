import heapq
from collections import deque


def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)

    n = len(jobs)
    hq = []
    now_time = 0

    while jobs or hq:
        if hq:
            now_work = heapq.heappop(hq)
            now_time += now_work[0]
            answer += now_time-now_work[1]
        else:
            new_work = jobs.popleft()
            now_time = new_work[0]
            heapq.heappush(hq, (new_work[1], new_work[0]))
        while jobs and jobs[0][0] <= now_time:
            new_work = jobs.popleft()
            heapq.heappush(hq, (new_work[1], new_work[0]))
    return answer//n


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]]))
print(solution([[0, 1], [2, 2], [2, 3]]))
print(solution([[0, 3], [4, 4], [5, 3], [7, 1]]))
