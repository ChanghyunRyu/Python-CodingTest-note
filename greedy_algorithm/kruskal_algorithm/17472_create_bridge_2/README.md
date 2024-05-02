## 17472번 다리 만들기 2

---

시간 제한: 1초, 메모리 제한: 512MB

섬으로 이루어진 나라가 있고, 모든 섬을 다리로 연결하려고 한다. 이 나라의 지도는 N×M 크기의 이차원 격자로 나타낼 수 있고, 격자의 각 칸은 땅이거나 바다이다.

섬은 연결된 땅이 상하좌우로 붙어있는 덩어리를 말하고, 아래 그림은 네 개의 섬으로 이루어진 나라이다. 색칠되어있는 칸은 땅이다.

다리는 바다에만 건설할 수 있고, 다리의 길이는 다리가 격자에서 차지하는 칸의 수이다. 다리를 연결해서 모든 섬을 연결하려고 한다. 섬 A에서 다리를 통해 섬 B로 갈 수 있을 때, 섬 A와 B를 연결되었다고 한다. 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안된다. 또, 다리의 길이는 2 이상이어야 한다.

다리의 방향이 중간에 바뀌면 안되기 때문에, 다리의 방향은 가로 또는 세로가 될 수 밖에 없다. 방향이 가로인 다리는 다리의 양 끝이 가로 방향으로 섬과 인접해야 하고, 방향이 세로인 다리는 다리의 양 끝이 세로 방향으로 섬과 인접해야 한다.

섬 A와 B를 연결하는 다리가 중간에 섬 C와 인접한 바다를 지나가는 경우에 섬 C는 A, B와 연결되어있는 것이 아니다. 


### 입력

- 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 지도의 정보가 주어진다. 
- 각 줄은 M개의 수로 이루어져 있으며, 수는 0 또는 1이다. 0은 바다, 1은 땅을 의미한다.
- 1 ≤ N, M ≤ 10
- 3 ≤ N×M ≤ 100
- 2 ≤ 섬의 개수 ≤ 6

### 출력

- 모든 섬을 연결하는 다리 길이의 최솟값을 출력한다. 
- 모든 섬을 연결하는 것이 불가능하면 -1을 출력한다.

---
1. dfs를 이용하여 각 섬의 번호를 매긴다.
2. bfs를 이용하여 각 섬으로 이동할 수 있는 다리를 체크하고 이를 이용하여 그래프를 만든다.
3. 만든 그래프를 이용하여 최소 신장 트리 알고리즘으로 정답을 구한다.
4. 이 때 각 노드의 방문 여부를 저장하여 모든 섬을 연결할 수 있는지 체크한다.
~~~
from collections import deque
import heapq
INF = int(1e9)

n, m = map(int, input().split())
# map 정보 입력
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# dfs 이용한 섬 개수 세기
def dfs(x, y, num):
    maps[x][y] = num
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if maps[nx][ny] == 1:
            dfs(nx, ny, num)


cnt = -1
for i in range(n):
    for j in range(m):
        if maps[i][j] == 1:
            dfs(i, j, cnt)
            cnt -= 1

cnt = cnt * (-1) - 1

# 가능한 다리 찾아서 그래프 형식 만들기
graph = [[INF] * (cnt + 1) for _ in range(cnt + 1)]
q = deque([])
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0:
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if ni < 0 or ni >= n or nj < 0 or nj >= m or maps[ni][nj] != 0:
                    continue
                # (다음 x 좌표, 다음 y 좌표, 시작섬 숫자, 방향, 다리 길이)
                q.append((ni, nj, maps[i][j], (dx[k], dy[k]), 1))
while q:
    now_x, now_y, number, direct, length = q.popleft()
    next_x = now_x + direct[0]
    next_y = now_y + direct[1]
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
        continue
    if maps[next_x][next_y] == 0:
        q.append((next_x, next_y, number, direct, length + 1))
    else:
        start_num = number * (-1)
        end_num = maps[next_x][next_y] * (-1)
        if length != 1 and graph[start_num][end_num] > length:
            graph[start_num][end_num] = length
            graph[end_num][start_num] = length

# 생성한 그래프 이용한 최소 신장 트리 만들기
q = []
start = 1
visited = [False]*(cnt+1)
heapq.heappush(q, (0, start))
result = 0
while q:
    cost, now = heapq.heappop(q)
    if not visited[now]:
        visited[now] = True
        result += cost
        for i in range(1, cnt+1):
            if i != now and graph[now][i] != INF and not visited[i]:
                heapq.heappush(q, (graph[now][i], i))
check = True
for i in range(1, cnt+1):
    if not visited[i]:
        check = False
if check:
    print(result)
else:
    print(-1)

~~~