## 2048(easy)

---

시간 제한: 1초, 메모리 제한: 512MB

2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다.
이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다. 이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다. 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다. 
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

이 문제에서 다루는 2048 게임은 보드의 크기가 N×N 이다. 보드의 크기와 보드판의 블록 상태가 주어졌을 때, 
최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다. 
- 둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다. 
- 0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다. 
- 블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다. 
- 블록은 적어도 하나 주어진다.

### 출력

- 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/22
- [ ] 2회
- [ ] 3회

flag를 만들어 놓고 활용을 잘못하여 시간이 오래 걸렸다.
~~~
import copy


def move_board(command, board_map):
    if command == 'UP':
        for y in range(n):
            temp = []
            flag = True
            for x in range(n):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    temp[-1] += board_map[x][y]
                    flag = False

            for i in range(n):
                if i >= len(temp):
                    board_map[i][y] = 0
                else:
                    board_map[i][y] = temp[i]
    elif command == 'DOWN':
        for y in range(n):
            temp = []
            flag = True
            for x in range(n-1, -1, -1):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    temp[-1] += board_map[x][y]
                    flag = False

            for i in range(n):
                if i >= len(temp):
                    board_map[n-i-1][y] = 0
                else:
                    board_map[n-i-1][y] = temp[i]
    elif command == 'LEFT':
        for x in range(n):
            temp = []
            flag = True
            for y in range(n):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    flag = False
                    temp[-1] += board_map[x][y]

            for i in range(n):
                if i >= len(temp):
                    board_map[x][i] = 0
                else:
                    board_map[x][i] = temp[i]
    else:
        for x in range(n):
            temp = []
            flag = True
            for y in range(n-1, -1, -1):
                if board_map[x][y] == 0:
                    continue
                if not temp or not flag or temp[-1] != board_map[x][y]:
                    flag = True
                    temp.append(board_map[x][y])
                elif flag and temp[-1] == board_map[x][y]:
                    flag = False
                    temp[-1] += board_map[x][y]

            for i in range(n):
                if i >= len(temp):
                    board_map[x][n-i-1] = 0
                else:
                    board_map[x][n-i-1] = temp[i]


def dfs(command, board_map, count, answer):
    move_board(command, board_map)
    if count == 5:
        answer.append(max(map(max, board_map)))
        return
    dfs('UP', copy.deepcopy(board_map), count + 1, answer)
    dfs('DOWN', copy.deepcopy(board_map), count + 1, answer)
    dfs('LEFT', copy.deepcopy(board_map), count + 1, answer)
    dfs('RIGHT', copy.deepcopy(board_map), count + 1, answer)


n = int(input())
board = [0*n for _ in range(n)]
for i in range(n):
    board[i] = list(map(int, input().split()))

result = []
dfs('UP', copy.deepcopy(board), 1, result)
dfs('DOWN', copy.deepcopy(board), 1, result)
dfs('LEFT', copy.deepcopy(board), 1, result)
dfs('RIGHT', copy.deepcopy(board), 1, result)
print(max(result))

~~~