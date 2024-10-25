## 톱니바퀴

---

시간 제한: 2초, 메모리 제한: 512MB

또, 톱니는 N극 또는 S극 중 하나를 나타내고 있다. 톱니바퀴에는 번호가 매겨져 있는데, 
가장 왼쪽 톱니바퀴가 1번, 그 오른쪽은 2번, 그 오른쪽은 3번, 가장 오른쪽 톱니바퀴는 4번이다.

이때, 톱니바퀴를 총 K번 회전시키려고 한다.
톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다. 
톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, 
B는 A가 회전한 방향과 반대방향으로 회전하게 된다. 

톱니바퀴의 초기 상태와 톱니바퀴를 회전시킨 방법이 주어졌을 때, 최종 톱니바퀴의 상태를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 1번 톱니바퀴의 상태, 
- 둘째 줄에 2번 톱니바퀴의 상태, 
- 셋째 줄에 3번 톱니바퀴의 상태, 
- 넷째 줄에 4번 톱니바퀴의 상태가 주어진다. 
- 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다. 
- N극은 0, S극은 1로 나타나있다.
- 다섯째 줄에는 회전 횟수 K(1 ≤ K ≤ 100)가 주어진다. 
- 다음 K개 줄에는 회전시킨 방법이 순서대로 주어진다. 
- 각 방법은 두 개의 정수로 이루어져 있고, 첫 번째 정수는 회전시킨 톱니바퀴의 번호, 두 번째 정수는 방향이다. 
- 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.

### 출력

- 총 K번 회전시킨 이후에 네 톱니바퀴의 점수의 합을 출력한다. 점수란 다음과 같이 계산한다.
  - 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
  - 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
  - 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
  - 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

---
### Problem Solved Check
- [x] 1회 24/10/25
- [ ] 2회
- [ ] 3회

톱니바퀴는 한 사이클에 한 번만 회전한다. 잘 읽어봤으면 알 수 있어 시간이 오래 걸리지 않았을 듯.
~~~

wheel = []
for _ in range(4):
    wheel.append(list(map(int, input())))

k = int(input())
rolls = []
for _ in range(k):
    rolls.append(map(int, input().split()))

wheel_left = [6]*4
wheel_right = [2]*4


def wheel_roll(number, direction, check):
    check[number] = True
    if number-1 >= 0 and not check[number-1] and wheel[number-1][wheel_right[number-1]] != wheel[number][wheel_left[number]]:
        wheel_roll(number-1, -direction, check)
    if number+1 < 4 and not check[number+1] and wheel[number+1][wheel_left[number+1]] != wheel[number][wheel_right[number]]:
        wheel_roll(number+1, -direction, check)
    wheel_right[number] = (wheel_right[number]-direction) % 8
    wheel_left[number] = (wheel_left[number]-direction) % 8


for num, d in rolls:
    wheel_roll(num-1, d, [False]*4)

answer = 0
for i in range(4):
    top = (wheel_right[i]-2) % 8
    answer += 2**i * wheel[i][top]
print(answer)

~~~