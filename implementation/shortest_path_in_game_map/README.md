## 게임 맵 최단거리

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/1844

ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 
따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

### 제한 사항

- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
  - n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

---
### Problem Solved Check
- [x] 1회 24/08/12 
- [ ] 2회
- [ ] 3회
~~~
from collections import deque


def solution(maps):
    answer = -1
    start = (0, 0)
    n = len(maps)
    m = len(maps[0])
    queue = deque([(start, 1)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        now, count = queue.popleft()
        if now[0] == n-1 and now[1] == m-1:
            answer = count
            break
        for i in range(4):
            nx = now[0]+dx[i]
            ny = now[1]+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            queue.append(((nx, ny), count+1))
            maps[nx][ny] = 0
    return answer
    
~~~