## K진수에서 소수 개수 구하기

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/92335

양의 정수 n이 주어집니다. 이 숫자를 k진수로 바꿨을 때, 
변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

- 0P0처럼 소수 양쪽에 0이 있는 경우
- P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
- 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
- P처럼 소수 양쪽에 아무것도 없는 경우
- 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
- 예를 들어, 101은 P가 될 수 없습니다.

### 제한 사항

- 1 ≤ n ≤ 1,000,000
- 3 ≤ k ≤ 10

---
### Problem Solved Check
- [x] 1회 24/08/27
- [ ] 2회
- [ ] 3회
~~~
import re


def solution(n, k):
    answer = 0
    k_number = conversion_k(n, k)
    for num in re.split('0+', k_number):
        if not num:
            continue
        if check_prime_number(int(num)):
            answer += 1
    return answer


def conversion_k(number, k):
    result = []
    while number >= k:
        result.append(str(number % k))
        number = number // k
    result.append(str(number))
    return ''.join(result[::-1])


def check_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, int(number*0.5)+1):
        if number % i == 0:
            return False
    return True
~~~