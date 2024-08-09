## 등굣길

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42898

계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 
즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 
오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 
최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
  - m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
- 물에 잠긴 지역은 0개 이상 10개 이하입니다.
- 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.
---
### Problem Solved Check
- [x] 1회 24/06/26
- [x] 2회 24/08/09
- [ ] 3회
~~~
def solution(m, n, puddles):
    way = [[0]*m for _ in range(n)]
    way[0][0] = 1
    for puddle in puddles:
        x, y = puddle[0]-1, puddle[1]-1
        way[y][x] = -1
    for p_y in range(len(way)):
        for p_x in range(len(way[p_y])):
            if way[p_y][p_x] == -1:
                continue
            if p_y-1 >= 0 and way[p_y-1][p_x] != -1:
                way[p_y][p_x] += way[p_y-1][p_x]
            if p_x-1 >= 0 and way[p_y][p_x-1] != -1:
                way[p_y][p_x] += way[p_y][p_x-1]
    print(way)
    return way[-1][-1] % 1000000007
    
~~~
~~~
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1 or (i == 0 and j == 0):
                continue
            left = up = 0
            if j-1 >= 0 and dp[i][j-1] != -1:
                left = dp[i][j-1]
            if i-1 >= 0 and dp[i-1][j] != -1:
                up = dp[i-1][j]
            dp[i][j] = (left+up) % 1000000007
    return dp[n-1][m-1]
    
~~~