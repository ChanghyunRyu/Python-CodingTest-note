## 1789번 수들의 합

---

시간 제한: 2초, 메모리 제한: 128MB

서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

### 입력

- 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

### 출력

- 첫째 줄에 자연수 N의 최댓값을 출력한다.

---
### Problem Solved Check
- [x] 1회 24/05/13
- [ ] 2회
- [ ] 3회
~~~
s = int(input())
n = 1
sum_of_num = 1
while True:
    n += 1
    sum_of_num += n
    if sum_of_num > s:
        break
print(n-1)

~~~