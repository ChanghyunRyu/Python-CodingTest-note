## 1206. [S/W 문제해결 기본] 1일차 - View

---

[문제] https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

---

### 풀이

### Problem Solved Check
- [x] 1회 24/11/16
- [ ] 2회
- [ ] 3회

~~~
for test_case in range(1, 11):
    N = int(input())
    b = list(map(int, input().split()))
    answer = 0
    for i in range(2, N-2):
        left = max(b[i-1], b[i-2])
        right = max(b[i+1], b[i+2])
        if left >= b[i] or right >= b[i]:
            continue
        answer += b[i] - max(left, right)
    print('#{} {}'.format(test_case, answer))

~~~