# 백준 2667번 문제 단지번호 붙이기
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def numbering_home(x, y):
    if graph[x][y] == 1:
        graph[x][y] = 2
        queue = deque()
        queue.append((x, y))
        count = 1
        while queue:
            x, y = queue.popleft()
            for index in range(4):
                nx = x + dx[index]
                ny = y + dy[index]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == 1:
                    count += 1
                    graph[nx][ny] = 2
                    queue.append((nx, ny))
        return count
    return 0


result = []
for i in range(n):
    for j in range(n):
        home = numbering_home(i, j)
        if not home == 0:
            result.append(home)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])
