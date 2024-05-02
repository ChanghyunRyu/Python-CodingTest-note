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
