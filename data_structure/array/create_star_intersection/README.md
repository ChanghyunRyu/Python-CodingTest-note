## 교점에 별 만들기

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/87377

Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

### 제한 사항

- line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
  - line의 가로(열) 길이는 3입니다.
  - line의 각 원소는 [A, B, C] 형태입니다.
  - A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
  - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
  - A = 0이면서 B = 0인 경우는 주어지지 않습니다.
- 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
- 별이 한 개 이상 그려지는 입력만 주어집니다.

---
~~~
def solution(line):
    answer = []
    point = []
    x_min = y_min = int(1e15)
    x_max= y_max = -int(1e15)
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d != b*c:
                # 교점 x, y 좌표 구하기
                x = float((b*f-e*d)/(a*d-b*c))
                y = float((e*c-a*f)/(a*d-b*c))
                if x.is_integer() and y.is_integer():
                    x = int(x)
                    y = int(y)
                    point.append([x, y])
                    if x_min > x:
                        x_min = x
                    if y_min > y:
                        y_min = y
                    if x_max < x:
                        x_max = x
                    if y_max < y:
                        y_max = y
    tmp = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for pos_x, pos_y in point:
        nx = pos_x - x_min
        ny = pos_y - y_min
        tmp[ny][nx] = '*'
    for t in tmp:
        answer.append(''.join(t))
    return answer[::-1]

~~~