## 경사로

---

시간 제한: 2초, 메모리 제한: 512MB

크기가 N×N인 지도가 있다. 지도의 각 칸에는 그 곳의 높이가 적혀져 있다.
오늘은 이 지도에서 지나갈 수 있는 길이 몇 개 있는지 알아보려고 한다

길은 총 2N개가 있으며, 길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 모두 같아야 한다. 
또는, 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 경사로는 높이가 항상 1이며, 길이는 L이다. 
또, 개수는 매우 많아 부족할 일이 없다. 경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

- 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
- 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
- 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다

아래와 같은 경우에는 경사로를 놓을 수 없다.

- 경사로를 놓은 곳에 또 경사로를 놓는 경우
- 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
- 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
- 경사로를 놓다가 범위를 벗어나는 경우

### 입력

- 첫째 줄에 N (2 ≤ N ≤ 100)과 L (1 ≤ L ≤ N)이 주어진다. 
- 둘째 줄부터 N개의 줄에 지도가 주어진다. 각 칸의 높이는 10보다 작거나 같은 자연수이다.

### 출력

- 첫째 줄에 지나갈 수 있는 길의 개수를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/23
- [ ] 2회
- [ ] 3회
~~~
import sys


def check_runway(line, need):
    check = [False]*len(line)
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i]-line[i+1]) > 1:
            return False
        # 경사로 설치할 수 있는지 체크
        if line[i] > line[i+1]:
            for step in range(1, need+1):
                ni = i+step
                if ni >= len(line):
                    return False
                if not check[ni]:
                    check[ni] = True
                else:
                    return False
        else:
            for step in range(1, need+1):
                ni = i-need+step
                if ni < 0:
                    return False
                if not check[ni]:
                    check[ni] = True
                else:
                    return False
    return True


n, runway = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for line in board:
    if check_runway(line, runway):
        answer += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    if check_runway(temp, runway):
        answer += 1
print(answer)

~~~
