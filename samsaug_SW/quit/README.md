## 퇴사

---

시간 제한: 2초, 메모리 제한: 512MB

상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
- 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

### 출력

- 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/10/23
- [ ] 2회
- [ ] 3회
~~~
n = int(input())
counsel = []
for i in range(1, n+1):
    day, amount = map(int, input().split())
    counsel.append((i, i+day, amount))

dp = [0]*(n+2)
for day in range(1, n+2):
    temp = 0
    for i in range(len(counsel)):
        start, end, amount = counsel[i]
        if end == day:
            temp = max(temp, max(dp[:start+1])+amount)
    dp[day] = temp

print(max(dp))

~~~
