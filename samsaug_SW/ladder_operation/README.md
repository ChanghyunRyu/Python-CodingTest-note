## 사다리 조작

---

사다리 게임은 N개의 세로선과 M개의 가로선으로 이루어져 있다. 인접한 세로선 사이에는 가로선을 놓을 수 있는데, 
각각의 세로선마다 가로선을 놓을 수 있는 위치의 개수는 H이고, 모든 세로선이 같은 위치를 갖는다.

사다리에 가로선을 추가해서, 사다리 게임의 결과를 조작하려고 한다. 이때, i번 세로선의 결과가 i번이 나와야 한다. 
그렇게 하기 위해서 추가해야 하는 가로선 개수의 최솟값을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 세로선의 개수 N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 H가 주어진다. (2 ≤ N ≤ 10, 1 ≤ H ≤ 30, 0 ≤ M ≤ (N-1)×H)
- 둘째 줄부터 M개의 줄에는 가로선의 정보가 한 줄에 하나씩 주어진다.
- 가로선의 정보는 두 정수 a과 b로 나타낸다. (1 ≤ a ≤ H, 1 ≤ b ≤ N-1) b번 세로선과 b+1번 세로선을 a번 점선 위치에서 연결했다는 의미이다.
- 가장 위에 있는 점선의 번호는 1번이고, 아래로 내려갈 때마다 1이 증가한다. 세로선은 가장 왼쪽에 있는 것의 번호가 1번이고, 오른쪽으로 갈 때마다 1이 증가한다.
- 입력으로 주어지는 가로선이 서로 연속하는 경우는 없다.

### 출력

- 번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력한다. 
- 만약, 정답이 3보다 큰 값이면 -1을 출력한다. 또, 불가능한 경우에도 -1을 출력한다.

---
### Problem Solved Check
- [ ] 1회 복습 필요
- [ ] 2회
- [ ] 3회

copy.deepcopy()는 생각보다 많은 시간이 소모된다. 시간 초과가 자주 나오는 백트래킹 문제에서는 안 쓰는 방법을 모색해 보는 것도 좋다.
~~~
import sys


n, m, h = map(int, sys.stdin.readline().split())
ladders = [[0]*n for _ in range(h)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ladders[a-1][b-1] = 1


def check_problem(number, ladder):
    for idx in range(number):
        start = idx
        for height in range(len(ladder)):
            if ladder[height][start] == 1:
                start += 1
            elif start > 0 and ladder[height][start-1] == 1:
                start -= 1
        if start != idx:
            return False
    return True


def dfs(count, x, ladder):
    global answer
    if answer <= count:
        return
    if check_problem(len(ladder[0]), ladder):
        answer = min(answer, count)
        return
    if count >= 3:
        return
    for i in range(x, len(ladder)):
        for j in range(0, len(ladder[0])-1):
            check_left = j == 0 or ladder[i][j-1] == 0
            check_right = ladder[i][j+1] == 0
            if ladder[i][j] == 0 and check_left and check_right:
                ladder[i][j] = 1
                dfs(count+1, i, ladder)
                ladder[i][j] = 0


answer = 4
dfs(0, 0, ladders)
if answer > 3:
    answer = -1
print(answer)

~~~