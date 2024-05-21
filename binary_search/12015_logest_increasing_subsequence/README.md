## 12015번 가장 긴 증가하는 부분 수열 2

---

시간 제한: 1초, 메모리 제한: 512MB

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

### 입력

- 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
- 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

### 출력

- 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/05/21
- [ ] 2회
- [ ] 3회
~~~
from bisect import bisect_left
INF = int(1e7)

n = int(input())
sequence = list(map(int, input().split()))
sub = [INF]
for s in sequence:
    if s > sub[len(sub)-1]:
        sub.append(s)
    else:
        index = bisect_left(sub, s)
        if sub[index] > s:
            sub[index] = s

print(len(sub))

~~~