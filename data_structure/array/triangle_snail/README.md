## 삼각 달팽이

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/68645

정수 n이 매개변수로 주어집니다. 
다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

### 제한 사항

- n은 1 이상 1,000 이하입니다.

---
### Problem Solved Check
- [x] 1회  
- [x] 2회 24/10/15
- [ ] 3회
~~~
def solution(n):
    answer = []
    # n의 크기를 가진 삼각형 만들기 만들기
    triangle = [[0]*i for i in range(1, n+1)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]

    # 현재 좌표, 카운트
    nx, ny = 0, 0
    cnt = 1
    end = n
    dx_idx, dy_idx = 0, 0
    for k in range(1, ((n**2+n)//2)+1):
        triangle[ny][nx] = k
        cnt += 1
        nx += dx[dx_idx]
        ny += dy[dy_idx]
        if cnt == end:
            cnt = 0
            end -= 1
            dx_idx = (dx_idx+1) % 3
            dy_idx = (dy_idx+1) % 3
    for tri in triangle:
        answer += tri
    return answer
~~~
~~~
def solution(n):
    direction = [[1, 0], [0, 1], [-1, -1]]
    snail = [[0]*(i+1) for i in range(n)]

    count = n
    point = [-1, 0]
    idx = 0
    num = 0
    while count != 0:
        for _ in range(count):
            num += 1
            point[0] += direction[idx][0]
            point[1] += direction[idx][1]
            snail[point[0]][point[1]] = num
        count -= 1
        idx = (idx+1) % 3
    return sum(snail, [])
~~~