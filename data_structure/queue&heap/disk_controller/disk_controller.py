import heapq
from collections import deque


def solution(jobs):
    jobs = sorted(jobs, key=lambda x: (x[0], x[1]))
    jobs = deque(jobs)

    q = []
    done = []

    while jobs:
        first_work = jobs.popleft()
        now_time = first_work[0]
        heapq.heappush(q, (first_work[1], first_work[0]))
        while q:
            task, start = heapq.heappop(q)
            now_time += task
            done.append(now_time - start)
            while len(jobs) != 0 and now_time >= jobs[0][0]:
                new_task = jobs.popleft()
                heapq.heappush(q, (new_task[1], new_task[0]))
    answer = int(sum(done)/len(done))
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[5, 10], [6, 8], [14, 2], [11, 5], [100, 7]]))
print(solution([[0, 1], [2, 2], [2, 3]]))
print(solution([[0, 3], [4, 4], [5, 3], [7, 1]]))
