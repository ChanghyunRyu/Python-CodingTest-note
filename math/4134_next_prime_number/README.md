## 4134번 다음 소수

---

시간 제한: 1초, 메모리 제한: 128MB

정수 n(0 ≤ n ≤ 4*109)가 주어졌을 때, n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 테스트 케이스의 개수가 주어진다. 
- 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다.

### 출력

- 각각의 테스트 케이스에 대해서 n보다 크거나 같은 소수 중 가장 작은 소수를 한 줄에 하나씩 출력한다.

---
~~~
test = int(input())


def find_next_prime(number):
    answer = number
    while not check_prime_number(answer):
        answer += 1
    return answer


def check_prime_number(number):
    if number == 1 or number == 0:
        return False
    end = int(number**0.5)
    for i in range(2, end+1):
        if number % i == 0:
            return False
    return True


for _ in range(test):
    n = int(input())
    next_prime = find_next_prime(n)
    print(next_prime)

~~~