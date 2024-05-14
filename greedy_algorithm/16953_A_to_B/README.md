## 16953번 A → B

---

시간 제한: 2초, 메모리 제한: 512MB

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
- 2를 곱한다.
- 1을 수의 가장 오른쪽에 추가한다. 

A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

### 입력

- 첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.

### 출력

- A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/05/14
- [ ] 2회
- [ ] 3회
~~~
from collections import deque

a, b = map(int, input().split())
q = deque([(a, 1)])
result = -1
while q:
    num, count = q.popleft()
    if num == b:
        result = count
        break
    if num*2 <= b:
        q.append((num*2, count+1))
    if (num*10)+1 <= b:
        q.append(((num*10)+1, count+1))
print(result)

~~~