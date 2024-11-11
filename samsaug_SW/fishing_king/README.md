## 낚시왕

---

시간 제한: 1초, 메모리 제한: 512MB

낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다. 격자판의 각 칸은 (r, c)로 나타낼 수 있다. r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다. 
칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.

낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다. 
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

1. 낚시왕이 오른쪽으로 한 칸 이동한다.
2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
3. 상어가 이동한다.

상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 
이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.

낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.

### 입력

- 첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
- 둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 
- 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다. 
- (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
- 두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

### 출력

- 낚시왕이 잡은 상어 크기의 합을 출력한다.

---
### Problem Solved Check
- [x] 1회 
- [ ] 2회
- [ ] 3회
~~~
import sys


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
r, c, m = map(int, input().split())
shark = {}


for _ in range(m):
    x1, y1, s, d, z = map(int, sys.stdin.readline().split())
    shark[(x1-1, y1-1)] = (s, d, z)


def move_shark(point, sp, di):
    x, y = point
    if di == UP or di == DOWN:
        cycle = 2*r-2
        sp %= cycle
        while sp > 0:
            if di == UP:
                if x-sp > 0:
                    x -= sp
                    sp = 0
                else:
                    sp -= x
                    x = 0
                    di = DOWN
            else:
                if x+sp < r:
                    x += sp
                    sp = 0
                else:
                    sp -= r-1-x
                    x = r-1
                    di = UP
    else:
        cycle = 2*c-2
        sp %= cycle
        while sp > 0:
            if di == RIGHT:
                if y+sp < c:
                    y += sp
                    sp = 0
                else:
                    sp -= c-1-y
                    y = c - 1
                    di = LEFT
            else:
                if y-sp > 0:
                    y -= sp
                    sp = 0
                else:
                    sp -= y
                    y = 0
                    di = RIGHT
    return (x, y), di


now = 0
answer = 0
while now < c:
    for i in range(r):
        if (i, now) in shark:
            answer += shark[(i, now)][2]
            del shark[(i, now)]
            break
    now += 1
    new_shark = {}
    for key in shark:
        speed, direction, size = shark[key]
        new_p, new_d = move_shark(key, speed, direction)
        if new_p not in new_shark:
            new_shark[new_p] = (speed, new_d, size)
        elif new_shark[new_p][2] < size:
            new_shark[new_p] = (speed, new_d, size)
    shark = new_shark
print(answer)

~~~