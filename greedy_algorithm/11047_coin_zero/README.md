## 11047번 동전 0

---

시간 제한: 1초, 메모리 제한: 256MB

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
- 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

### 출력

- 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.

---

### Problem Solved Check

- [x] 1회: 24/05/09
- [ ] 2회
- [ ] 3회

처음에 몫/나머지로 한번에 뺀다는 생각을 못하고 하나씩 빼면서 시간초과 오류가 발생.

~~~
import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

change = k
count = 0
i = len(coins)-1
while change > 0:
    if change < coins[i]:
        i -= 1
        continue
    quo = change//coins[i]
    change %= coins[i]
    count += quo
print(count)

~~~