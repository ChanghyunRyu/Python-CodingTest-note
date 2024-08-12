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


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
