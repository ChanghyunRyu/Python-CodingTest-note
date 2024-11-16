## 1244. [S/W 문제해결 응용] 2일차 - 최대 상금

---

[문제] https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

---
### 풀이
### Problem Solved Check
- [x] 1회 24/11/16
- [ ] 2회
- [ ] 3회
~~~
from itertools import combinations


T = int(input())


def dfs(depth, nums):
    if depth == change:
        return nums
    new_nums = set()
    for num in nums:
        for a, b in combinations(list(range(len(num))), 2):
            new_num = list(num)
            new_num[a], new_num[b] = new_num[b], new_num[a]
            new_nums.add(''.join(new_num))
    return dfs(depth+1, new_nums)


for test_case in range(1, T + 1):
    number, change = input().split()
    change = int(change)
    numbers = set([number])
    r = dfs(0, numbers)
    answer = max(r)
    print('#{} {}'.format(test_case, answer))

~~~