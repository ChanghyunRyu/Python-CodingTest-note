## 소수 찾기

---

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 
종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

---
### Problem Solved Check
- [x] 1회 24/06/12
- [x] 2회 24/08/01
- [ ] 3회

순열을 통해 숫자를 뽑아내는 것을 생각해내긴했지만 이를 통해 숫자를 만드는 과정은 매끄럽지 못 했다.

~~~
import itertools


def solution(numbers):
    answer = set()
    temp = []
    for n in numbers:
        temp.append(int(n))
    numbers = temp
    for i in range(1, len(numbers)+1):
        npi = list(itertools.permutations(numbers, i))
        for np in npi:
            np = list(np)
            if len(np) == 1:
                num = np[0]
            else:
                num = int(''.join(list(map(str, np))))
            if num not in answer and chk_prime_number(num):
                answer.add(num)
    return len(answer)


def chk_prime_number(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

~~~
~~~
import itertools


def solution(numbers):
    answer = set()
    for i in range(1, len(numbers)+1):
        for permutation in itertools.permutations(numbers, i):
            permutation = list(permutation)
            number = int(''.join(permutation))
            if get_prime_numbers(number):
                answer.add(number)
    return len(answer)


def get_prime_numbers(number):
    m = int(number**0.5)
    if number == 0 or number == 1:
        return False
    for i in range(2, m+1):
        if number % i == 0:
            return False
    return True

~~~
