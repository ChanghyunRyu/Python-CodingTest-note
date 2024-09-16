## 파괴되지 않는 건물

---

N x M 크기의 행렬 모양의 게임 맵이 있습니다. 
이 맵에는 내구도를 가진 건물이 각 칸마다 하나씩 있습니다. 
적은 이 건물들을 공격하여 파괴하려고 합니다. 
건물은 적의 공격을 받으면 내구도가 감소하고 내구도가 0이하가 되면 파괴됩니다. 
반대로, 아군은 회복 스킬을 사용하여 건물들의 내구도를 높이려고 합니다.

건물의 내구도를 나타내는 2차원 정수 배열 board와 
적의 공격 혹은 아군의 회복 스킬을 나타내는 2차원 정수 배열 skill이 
매개변수로 주어집니다. 적의 공격 혹은 아군의 회복 스킬이 모두 끝난 뒤 
파괴되지 않은 건물의 개수를 return하는 solution함수를 완성해 주세요.

### 제한 사항

- 1 ≤ board의 행의 길이 (= N) ≤ 1,000
- 1 ≤ board의 열의 길이 (= M) ≤ 1,000
- 1 ≤ board의 원소 (각 건물의 내구도) ≤ 1,000
- 1 ≤ skill의 행의 길이 ≤ 250,000
- skill의 열의 길이 = 6
- skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.
  - type은 1 혹은 2입니다.
    - type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
    - type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.
  - (r1, c1)부터 (r2, c2)까지 직사각형 모양의 범위 안에 있는 건물의 내구도를 degree 만큼 낮추거나 높인다는 뜻입니다.
    - 0 ≤ r1 ≤ r2 < board의 행의 길이
    - 0 ≤ c1 ≤ c2 < board의 열의 길이
    - 1 ≤ degree ≤ 500
    - type이 1이면 degree만큼 건물의 내구도를 낮춥니다.
    - type이 2이면 degree만큼 건물의 내구도를 높입니다.
- 건물은 파괴되었다가 회복 스킬을 받아 내구도가 1이상이 되면 파괴되지 않은 상태가 됩니다. 즉, 최종적으로 건물의 내구도가 1이상이면 파괴되지 않은 건물입니다.

---
### Problem Solved Check
- [X] 1회  24/09/16
- [ ] 2회
- [ ] 3회

누적합을 이용하여 좌표부터 좌표까지의 값 업데이트를 간단하게 하는 방법을 배웠다.
~~~
def solution(board, skill):
    answer = 0
    prefix_sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for i in range(len(skill)):
        correction_skill(prefix_sum, skill[i])

    for i in range(len(prefix_sum)-1):
        for j in range(len(prefix_sum[0])-1):
            prefix_sum[i][j+1] += prefix_sum[i][j]
    for j in range(len(prefix_sum[0])-1):
        for i in range(len(prefix_sum)-1):
            prefix_sum[i+1][j] += prefix_sum[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer


def correction_skill(board, skill):
    t, x1, y1, x2, y2, degree = skill
    if t == 1:
        degree *= -1
    board[x1][y1] += degree
    board[x1][y2+1] += -degree
    board[x2+1][y1] += -degree
    board[x2+1][y2+1] += degree
    
~~~