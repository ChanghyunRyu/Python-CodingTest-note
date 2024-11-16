## 5215. 햄버거 다이어트 

---

[문제] https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

---
### 풀이
### Problem Solved Check
- [x] 1회 24/11/16
- [ ] 2회
- [ ] 3회

전형적인 냅색 문제, 간만에 풀어서 그런지 버벅였다.
~~~
T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    foods = []
    for _ in range(N):
        foods.append(list(map(int, input().split())))
   	
    dp = [[0]*(L+1) for _ in range(N+1)]
    for i in range(1, N+1):
        score, kcal = foods[i-1]
        for w in range(1, L+1):
            if w < kcal:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w-kcal]+score, dp[i-1][w])
    answer = dp[N][L]
    print('#{} {}'.format(test_case, answer))

~~~