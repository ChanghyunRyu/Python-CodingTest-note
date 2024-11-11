from collections import deque
from collections import defaultdict
INF = int(1e9)

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

size = 2
now_x, now_y = 0, 0
fish = defaultdict(set)
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[i][j] = 0
        elif array[i][j] != 0:
            fish[array[i][j]].add((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_path():
    dist = [[-1]*n for _ in range(n)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            check = 0 <= nx < n and 0 <= ny < n
            if check and dist[nx][ny] == -1 and array[nx][ny] <= size:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
    return dist


answer = 0
ate = 0
while True:
    # 거리 구하기
    dist = find_path()

    # 먹을 수 있는 물고기 찾기
    temp = set()
    for i in range(1, size):
        temp |= fish[i]

    min_dist = INF
    for fx, fy in temp:
        if dist[fx][fy] != -1:
            if dist[fx][fy] < min_dist:
                next_x, next_y = fx, fy
                min_dist = dist[fx][fy]
            elif dist[fx][fy] == min_dist:
                if fx < next_x:
                    next_x, next_y = fx, fy
                elif fx == next_x and fy < next_y:
                    next_x, next_y = fx, fy

    if min_dist == INF:
        break

    now_x, now_y = next_x, next_y
    answer += dist[next_x][next_y]

    ate += 1
    if ate == size:
        size += 1
        ate = 0
    fish[array[next_x][next_y]].remove((next_x, next_y))
    array[next_x][next_y] = 0

print(answer)
