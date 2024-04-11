## 13549번 숨박꼭질 3

---

시간 제한: 2초, 메모리 제한: 512MB

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

### 입력

- 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. 
- N과 K는 정수이다.

### 출력

- 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

### 힌트

- 입력이 5 17일때, 수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.

---

### BFS를 이용한 방법
~~~
from collections import deque
INF = int(1e9)

n, k = map(int, input().split())
result = [INF for _ in range(100001)]
result[n] = 0
q = deque()
q.append(n)

while q:
    now = q.popleft()
    if now == k:
        break
    if 0 <= (now-1) < 100001 and result[now-1] == INF:
        result[now-1] = result[now]+1
        q.append(now-1)
    if 0 <= (now*2) < 100001 and result[now*2] > result[now] + 1:
        result[now*2] = result[now]
        q.appendleft(now*2)
    if 0 <= (now+1) < 100001 and result[now+1] > result[now]+1:
        result[now+1] = result[now]+1
        q.append(now+1)

print(result[k])

~~~
  

### 다익스트라 알고리즘 + 우선순위 큐를 이용한 방법
~~~
import heapq
INF = int(1e9)

n, k = map(int, input().split())
result = [INF]*100001
result[n] = 0
q = []
heapq.heappush(q, (0, n))

while q:
    cost, now = heapq.heappop(q)
    if now == k:
        break
    if 0 <= now-1 and result[now-1] > cost+1:
        result[now-1] = cost+1
        heapq.heappush(q, (cost+1, now-1))
    if now*2 < 100001 and result[2*now] > cost:
        result[now*2] = cost
        heapq.heappush(q, (cost, now*2))
    if now+1 < 100001 and result[now+1] > cost+1:
        result[now+1] = cost+1
        heapq.heappush(q, (cost+1, now+1))

print(result[k])

~~~
