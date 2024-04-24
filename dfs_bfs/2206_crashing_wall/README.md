## 2206번 벽 부수고 이동하기

---

시간 제한: 2초, 메모리 제한: 192MB

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. 
- (1, 1)과 (N, M)은 항상 0이라고 가정하자.

### 출력

- 첫째 줄에 최단 거리를 출력한다. 
- 불가능할 때는 -1을 출력한다.

---
벽을 한번도 부수지 않은 경우, 벽을 한번이라도 부순 경우의 경로 두가지를 모두 저장하며 이동하는 것을 생각하지 못 함.  
DFS, BFS의 경우(노드를 이동할 때 비용계산을 하지 않을 경우) 각 노드의 탐색여부정도만 체크하는 것이 좋음.

~~~
import sys
from collections import deque
INF = int(1e9)

n, m = map(int, input().split())
arr = []
guidance = [[[INF]*2 for _ in range(m)] for _ in range(n)]
guidance[0][0][0] = 1
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip()))
    arr.append(line)

q = deque([(0, 0, 0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
while q:
    x, y, check = q.popleft()
    if x == n-1 and y == m-1:
        print(guidance[n-1][m-1][check])
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] == 1 and check == 0:
            guidance[nx][ny][1] = guidance[x][y][0]+1
            q.append((nx, ny, 1))
        if arr[nx][ny] == 0 and guidance[nx][ny][check] == INF:
            guidance[nx][ny][check] = guidance[x][y][check]+1
            if check == 0:
                guidance[nx][ny][1] = guidance[nx][ny][0]
            q.append((nx, ny, check))
if guidance[n-1][m-1][1] == INF and guidance[n-1][m-1][0] == INF:
    print(-1)

~~~