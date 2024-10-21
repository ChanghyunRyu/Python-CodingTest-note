## 구슬 탈출 2

---

시간 제한: 2초, 메모리 제한: 512MB

스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다. 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.

보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다.

이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.

각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.

보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

### 입력

- 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 
- 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 
- 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. 
- '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 
- 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
- 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.

### 출력

- 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 
- 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/21
- [ ] 2회
- [ ] 3회

result = min(answer) 에서 answer이 빈 배열일 경우, value error가 발생하는 오류를 못 찾았었음. 
~~~
def dfs(command, red, blue, hole, board, count, before_points, answer):
    if count > 10:
        return
    dx, dy = set_dxy(command)
    r_x, r_y = red
    b_x, b_y = blue
    flag = True
    b_in_hole = False
    r_in_hole = False
    while flag:
        flag = False
        b_nx = b_x + dx
        b_ny = b_y + dy
        if (b_nx, b_ny) == hole:
            b_in_hole = True
        if board[b_nx][b_ny] == 0 and (b_nx, b_ny) != (r_x, r_y):
            flag = True
            b_x = b_nx
            b_y = b_ny

        r_nx = r_x + dx
        r_ny = r_y + dy
        if (r_nx, r_ny) == hole:
            r_in_hole = True
        if board[r_nx][r_ny] == 0 and (r_nx, r_ny) != (b_x, b_y):
            flag = True
            r_x = r_nx
            r_y = r_ny
    if b_in_hole:
        return
    if r_in_hole:
        answer.append(count)
        return
    rb_point = ((r_x, r_y), (b_x, b_y))
    if rb_point in before_points:
        if before_points[rb_point] <= count:
            return
        else:
            before_points[rb_point] = count
    else:
        before_points[rb_point] = count

    dfs('UP', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('DOWN', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('LEFT', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)
    dfs('RIGHT', (r_x, r_y), (b_x, b_y), hole, board, count + 1, before_points, answer)


def set_dxy(command):
    if command == 'UP':
        return -1, 0
    elif command == 'DOWN':
        return 1, 0
    elif command == 'LEFT':
        return 0, -1
    elif command == 'RIGHT':
        return 0, 1


n, m = map(int, input().split())
bead_map = [[1]*m for _ in range(n)]

R_point = (0, 0)
B_point = (0, 0)
hole = (0, 0)
for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == '.':
            bead_map[i][j] = 0
        elif line[j] == 'R':
            bead_map[i][j] = 0
            R_point = (i, j)
        elif line[j] == 'B':
            bead_map[i][j] = 0
            B_point = (i, j)
        elif line[j] == 'O':
            bead_map[i][j] = 0
            hole = (i, j)

record = {(R_point, B_point): 0}
answer = [11]
dfs('UP', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('DOWN', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('LEFT', R_point, B_point, hole, bead_map, 1, record, answer)
dfs('RIGHT', R_point, B_point, hole, bead_map, 1, record, answer)
result = min(answer)
if result > 10:
    print(-1)
else:
    print(result)

~~~

