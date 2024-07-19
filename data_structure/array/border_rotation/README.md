## 행렬 테두리 회전하기

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/77485

rows x columns 크기인 행렬이 있습니다. 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다. 각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현하며, 그 의미는 다음과 같습니다.

- x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전합니다.

### 제한 사항

- rows는 2 이상 100 이하인 자연수입니다.
- columns는 2 이상 100 이하인 자연수입니다.
- 처음에 행렬에는 가로 방향으로 숫자가 1부터 하나씩 증가하면서 적혀있습니다.
  - 즉, 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j)입니다.
- queries의 행의 개수(회전의 개수)는 1 이상 10,000 이하입니다.
- queries의 각 행은 4개의 정수 [x1, y1, x2, y2]입니다.
  - x1 행 y1 열부터 x2 행 y2 열까지 영역의 테두리를 시계방향으로 회전한다는 뜻입니다.
  - 1 ≤ x1 < x2 ≤ rows, 1 ≤ y1 < y2 ≤ columns입니다.
  - 모든 회전은 순서대로 이루어집니다.
  - 예를 들어, 두 번째 회전에 대한 답은 첫 번째 회전을 실행한 다음, 그 상태에서 두 번째 회전을 실행했을 때 이동한 숫자 중 최솟값을 구하면 됩니다.

---
### Problem Solved Check
- [x] 1회 24/07/19 
- [ ] 2회
- [ ] 3회
~~~
def solution(rows, columns, queries):
    answer = []
    # 숫자로 된 배열 만들기
    arr = []
    for i in range(rows):
        arr.append(list(range(i*columns+1, (i+1)*columns+1)))
    # query 별로 회전 시키기
    for start_x, start_y, end_x, end_y in queries:
        now_x, now_y = start_x-1, start_y
        before_num = arr[now_x][now_y-1]
        min_num = before_num
        while True:
            # 저장한 기존 칸의 수와 새로운 index 의 수 교체
            before_num, arr[now_x][now_y] = arr[now_x][now_y], before_num
            min_num = min(min_num, before_num)
            if now_x == start_x-1 and now_y == start_y-1:
                break
            # 다음 칸으로 이동
            if now_x == start_x-1 and now_y < end_y-1:
                now_y += 1
            elif now_y == end_y-1 and now_x < end_x-1:
                now_x += 1
            elif now_x == end_x-1 and now_y > start_y-1:
                now_y -= 1
            elif now_y == start_y-1:
                now_x -= 1

        answer.append(min_num)
    return answer
~~~
~~~
def solution(rows, columns, queries):
    arr = [list(range(i*columns+1, (i+1)*columns+1)) for i in range(rows)]
    answer = []
    for q in queries:
        start = (q[0]-1, q[1]-1)
        end = (q[2]-1, q[3]-1)
        arr, result = rotate_arr(start, end, arr)
        answer.append(result)
    return answer


def rotate_arr(start, end, arr):
    before_num = arr[start[0]][start[1]]
    min_num = before_num
    # 상단 이동, start = (1, 1), end(4, 3)
    for i in range(start[1]+1, end[1]+1):
        before_num, arr[start[0]][i] = arr[start[0]][i], before_num
        min_num = min(min_num, before_num)
    # 우측 이동
    for i in range(start[0]+1, end[0]+1):
        before_num, arr[i][end[1]] = arr[i][end[1]], before_num
        min_num = min(min_num, before_num)
    # 하단 이동
    for i in range(end[1]-1, start[1]-1, -1):
        before_num, arr[end[0]][i] = arr[end[0]][i], before_num
        min_num = min(min_num, before_num)
    # 좌측 이동
    for i in range(end[0]-1, start[0]-1, -1):
        before_num, arr[i][start[1]] = arr[i][start[1]], before_num
        min_num = min(min_num, before_num)
    return arr, min_num


query = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
print(solution(6, 6, query))
query = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
print(solution(3, 3, query))

~~~