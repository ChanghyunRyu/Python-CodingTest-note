## 테트로미노

---

시간 제한: 2초, 메모리 제한: 512MB

폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.

- 정사각형은 서로 겹치면 안 된다.
- 도형은 모두 연결되어 있어야 한다.
- 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.

정사각형 4개를 이어 붙인 폴리오미노는 테트로미노라고 하며, 다음과 같은 5가지가 있다.

아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 
각각의 칸에는 정수가 하나 쓰여 있다.

테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

### 입력

- 첫째 줄에 종이의 세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
- 둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.


### 출력

- 첫째 줄에 테트로미노가 놓인 칸에 쓰인 수들의 합의 최댓값을 출력한다.
---
### Problem Solved Check
- [x] 1회 24/10/24
- [ ] 2회
- [ ] 3회

dfs 와 우선순위 큐를 사용한 방법을 하려했으나 긴 테트리스에서 대응을 못하는 문제가 생겨 단순한 방법으로 문제를 풀었다.
내일은 원래 하려던 방법을 사용하여 다시 풀어봐야겠음.
~~~
import sys
import heapq


tetris=[[(0, 0), (0, 1), (0, 2), (0, 3)],\
        [(0, 0), (1, 0), (2, 0), (3, 0)],\
        [(0, 0), (1, 0), (0, 1), (1, 1)],\
        [(0, 0), (1, 0), (2, 0), (2, 1)],\
        [(0, 0), (1, 0), (2, 0), (2, -1)],\
        [(0, 0), (0, 1), (1, 1), (2, 1)],\
        [(0, 0), (0, 1), (1, 0),(2, 0)],\
        [(0, 0), (1, 0), (1, 1), (1, 2)],\
        [(0, 0), (1, -1), (1, 0), (1, -2)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,0),(1,0),(1,-1),(2,-1)],\
        [(0,0),(0,1),(-1,1),(-1,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,0),(1,-1),(1,0),(1,1)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,0),(1,0),(1,-1),(2,0)]]


def search_tet(x, y, board_map):
    result = 0
    for tet in tetris:
        temp = 0
        flag = False
        for i in range(4):
            nx = x+tet[i][0]
            ny = x+tet[i][1]
            check = 0 <= nx < len(board_map) and 0 <= ny < len(board_map[0])
            if not check:
                flag = True
                break
            temp += board_map[nx][ny]
        if flag:
            continue
        result = max(result, temp)
    return result


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for i in range(n):
    for j in range(m):
        answer = max(answer, search_tet(i, j, board))
print(answer)

~~~
