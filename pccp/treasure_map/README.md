## 보물 지도

---

[출처] https://school.programmers.co.kr/learn/courses/15009/lessons/121690

진수는 보물이 묻힌 장소와 함정이 표시된 보물 지도를 이용해 보물을 찾으려 합니다. 
보물지도는 가로 길이가 n, 세로 길이가 m인 직사각형 모양입니다.

맨 왼쪽 아래 칸의 좌표를 (1, 1)으로, 맨 오른쪽 위 칸의 좌표를 (n, m)으로 나타냈을 때, 
보물은 (n, m) 좌표에 묻혀있습니다. 또한, 일부 칸에는 함정이 있으며, 해당 칸으로는 지나갈 수 없습니다.

진수는 처음에 (1, 1) 좌표에서 출발해 보물이 있는 칸으로 이동하려 합니다. 
이동할 때는 [상,하,좌,우]로 인접한 네 칸 중 한 칸으로 걸어서 이동합니다. 
한 칸을 걸어서 이동하는 데 걸리는 시간은 1입니다.

진수는 보물이 위치한 칸으로 수월하게 이동하기 위해 신비로운 신발을 하나 준비했습니다. 
이 신발을 신고 뛰면 한 번에 두 칸을 이동할 수 있으며, 함정이 있는 칸도 넘을 수 있습니다. 
하지만, 이 신발은 한 번밖에 사용할 수 없습니다. 신비로운 신발을 사용하여 뛰어서 두 칸을 이동하는 시간도 1입니다.

진수의 보물지도가 표현하는 지역의 가로 길이를 나타내는 정수 n, 
세로 길이를 나타내는 정수 m, 함정의 위치를 나타내는 2차원 정수 배열 hole이 주어졌을 때, 
진수가 보물이 있는 칸으로 이동하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 
단, 보물이 있는 칸으로 이동할 수 없다면, -1을 return 해야 합니다.

---
### Problem Solved Check
- [x] 1회 24/09/23
- [x] 2회 24/11/15
- [ ] 3회

bfs를 하는 경우, 큐에서 빼낸 이후 방문 처리를 해주면 쓸 데 없는 큐가 많이 늘어날 수 있다.
방문 처리를 해주면서 큐에 넣어줄 것.
~~~
from collections import deque


INF = int(1e9)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(n, m, hole):
    treasure_map = [[0] * m for _ in range(n)]
    dp = [[[INF] * 2 for _ in range(m)] for _ in range(n)]
    for x, y in hole:
        treasure_map[x - 1][y - 1] = 1

    q = deque([(0, 0, 0)])
    dp[0][0][0] = 0
    dp[0][0][1] = 0
    while q:
        x, y, magic_shoes= q.popleft()
        if x == n - 1 and y == m - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            check = 0 <= nx < n and 0 <= ny < m
            if check and dp[nx][ny][magic_shoes] == INF and treasure_map[nx][ny] == 0:
                dp[nx][ny][magic_shoes] = dp[x][y][magic_shoes] + 1
                q.append((nx, ny, magic_shoes))
            if not magic_shoes:
                nx = x + 2 * dx[i]
                ny = y + 2 * dy[i]
                check = 0 <= nx < n and 0 <= ny < m
                if check and dp[nx][ny][1] == INF and treasure_map[nx][ny] == 0:
                    dp[nx][ny][1] = dp[x][y][magic_shoes] + 1
                    q.append((nx, ny, 1))
    answer = min(dp[n - 1][m - 1])
    if answer == INF:
        return -1
    else:
        return answer
        
~~~
