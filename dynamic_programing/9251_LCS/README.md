## 9251번 LCS

---

시간 제한: 0.1초, 2초(Python), 메모리 제한: 256MB

LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

### 입력

- 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 
- 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

### 출력

- 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

---
~~~
txt1 = input()
txt2 = input()

dp = [[0]*(len(txt1)+1) for _ in range(len(txt2)+1)]
for i in range(1, len(txt1)+1):
    for j in range(1, len(txt2)+1):
        if txt1[i-1] == txt2[j-1]:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])
print(dp[len(txt2)][len(txt1)])

~~~