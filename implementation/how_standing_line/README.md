## 줄 서는 방법

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/12936

n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. 
n명이 사람을 줄을 서는 방법은 여러 가지 방법이 있습니다. 
예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

- [1, 2, 3]
- [1, 3, 2]
- [2, 1, 3]
- [2, 3, 1]
- [3, 1, 2]
- [3, 2, 1]

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, 
k번째 방법을 return하는 solution 함수를 완성해주세요.

사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, 
k번째 방법을 return하는 solution 함수를 완성해주세요.

---
### Problem Solved Check
- [x] 1회 24/07/25
- [x] 2회 24/10/14
- [ ] 3회
~~~
from math import factorial


def solution(n, k):
    answer = []
    numbers = list(range(1, n+1))
    k -= 1
    while numbers:
        idx, k = divmod(k, factorial(len(numbers)-1))
        answer.append(numbers.pop(idx))
    return answer
    
~~~