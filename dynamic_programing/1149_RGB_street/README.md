### RGB 거리

---
시간제한: 0.5초, 메모리 제한: 128MB

RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

### 입력

- 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다.
- 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다.
- 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

### 출력
- 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

---

~~~
import sys

n = int(input())
paint = []
for _ in range(n):
    paint.append(list(map(int, sys.stdin.readline().split())))

price_red = [0]*n
price_green = [0]*n
price_blue = [0]*n
price_red[0], price_green[0], price_blue[0] = paint[0][0], paint[0][1], paint[0][2]

for i in range(1, n):
    price_red[i] = min(price_blue[i-1], price_green[i-1]) + paint[i][0]
    price_green[i] = min(price_red[i-1], price_blue[i-1]) + paint[i][1]
    price_blue[i] = min(price_red[i-1], price_green[i-1]) + paint[i][2]

print(min(price_red[n-1], price_green[n-1], price_blue[n-1]))

~~~
