### 1209. [S/W 문제해결 기본] 2일차 - Sum

[문제] https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

---
### 풀이
### Problem Solved Check
- [x] 1회 24/11/16
- [ ] 2회
- [ ] 3회

SWEA D3 문제들을 풀어보는데 솔직히 왜 사람들이 잘 안 쓰는지 알거 같다. 일부러 그런건지 입출력 템플릿이 매번 들쑥날쑥에 가독성도 안 좋고 문제 질도 영...
~~~
T = 10

for _ in range(1, T + 1):
    test_case = int(input())
    n = 100
    numbers = []
    result = -1
    for _ in range(n):
        numbers.append(list(map(int, input().split())))
    col_sum = [0]*n
    d1 = d2 = 0
    for i in range(n):
        result = max(result, sum(numbers[i]))
        d1 += numbers[i][i]
        d2 += numbers[n-1-i][i]
        for j in range(n):
            col_sum[j] += numbers[i][j]
    result = max(result, d1, d2, max(col_sum))
    print('#{} {}'.format(test_case, result))

~~~