## 1450번 냅색문제

---

시간 제한: 1초, 메모리 제한: 128MB

세준이는 N개의 물건을 가지고 있고, 최대 C만큼의 무게를 넣을 수 있는 가방을 하나 가지고 있다.
N개의 물건을 가방에 넣는 방법의 수를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 N과 C가 주어진다. 
- N은 30보다 작거나 같은 자연수, C는 10^9보다 작거나 같은 음이 아닌 정수이다. 
- 둘째 줄에 물건의 무게가 주어진다. 무게도 10^9보다 작거나 같은 자연수이다.

### 출력

- 첫째 줄에 가방에 넣는 방법의 수를 출력한다.

---
### Problem Solved Check
- [ ] 1회 
- [ ] 2회
- [ ] 3회

~~~
from itertools import combinations
from bisect import bisect_right

n, c = map(int, input().split())
items = list(map(int, input().split()))
index = n//2

a = items[:index]
b = items[index:]
a_list = [0]
b_list = [0]
for i in range(1, len(a)+1):
    for com in combinations(a, i):
        a_list.append(sum(com))

for i in range(1, len(b)+1):
    for com in combinations(b, i):
        b_list.append(sum(com))
b_list.sort()
count = 0

for i in a_list:
    count += bisect_right(b_list, c-i)
print(count)

~~~