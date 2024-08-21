## 디스크 컨트롤러

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42627

하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 
작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 
평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

### 제한 사항

- jobs의 길이는 1 이상 500 이하입니다.
- jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
- 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
- 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
- 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

---
### Problem Solved Check
- [x] 1회 24/07/02 
- [x] 2회 24/08/21
- [ ] 3회
~~~
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
    
~~~
~~~
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
    
~~~
