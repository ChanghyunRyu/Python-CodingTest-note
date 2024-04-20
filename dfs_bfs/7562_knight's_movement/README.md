## 7562번 나이트의 이동

---

체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

### 입력

- 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
- 각 테스트 케이스는 세 줄로 이루어져 있다. 
- 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 
- 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
- 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

### 출력

- 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.

---

~~~
import sys
from collections import deque
INF = int(1e9)

T = int(input())
result = []
for _ in range(T):
    l = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    q = deque([start])
    board = [[INF]*l for _ in range(l)]
    board[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        if x == end[0] and y == end[1]:
            result.append(board[x][y])
            break
        if x+2 < l and y-1 >= 0 and board[x+2][y-1] > board[x][y]+1:
            board[x+2][y-1] = board[x][y]+1
            q.append((x+2, y-1))
        if x+2 < l and y+1 < l and board[x+2][y+1] > board[x][y]+1:
            board[x+2][y+1] = board[x][y]+1
            q.append((x+2, y+1))
        if x+1 < l and y-2 >= 0 and board[x+1][y-2] > board[x][y]+1:
            board[x+1][y-2] = board[x][y]+1
            q.append((x+1, y-2))
        if x+1 < l and y+2 < l and board[x+1][y+2] > board[x][y]+1:
            board[x+1][y+2] = board[x][y]+1
            q.append((x+1, y+2))
        if x-1 >= 0 and y+2 < l and board[x-1][y+2] > board[x][y]+1:
            board[x-1][y+2] = board[x][y]+1
            q.append((x-1, y+2))
        if x-2 >= 0 and y+1 < l and board[x-2][y+1] > board[x][y]+1:
            board[x-2][y+1] = board[x][y]+1
            q.append((x-2, y+1))
        if x-1 >= 0 and y-2 >= 0 and board[x-1][y-2] > board[x][y]+1:
            board[x-1][y-2] = board[x][y]+1
            q.append((x-1, y-2))
        if x-2 >= 0 and y-1 >= 0 and board[x-2][y-1] > board[x][y]+1:
            board[x-2][y-1] = board[x][y]+1
            q.append((x-2, y-1))

for r in result:
    print(r)

~~~
