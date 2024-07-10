## 17103번 골드바흐 파티션

---

시간 제한: 0.5초, 메모리 제한: 512MB

- 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 
짝수 N이 주어졌을 때, 골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.

### 입력

- 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 
- 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.

### 출력

- 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.

---
~~~
import sys


def return_prime_number(number):
    is_prime = [True]*number
    is_prime[1] = False
    end = int(number**0.5)
    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i+i, number, i):
                is_prime[j] = False
    return [i for i in range(2, number) if is_prime[i]]


def find_goldbach_partition(number, prime):
    prime_numbers = prime
    start, end = 0, len(prime_numbers)-1
    answer = 0
    while start <= end:
        cal = prime_numbers[start]+prime_numbers[end]
        if cal == number:
            answer += 1
            start += 1
        elif cal > number:
            end -= 1
        elif cal < number:
            start += 1
    return answer


t = int(input())
prime_number = return_prime_number(1000000)
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    partitions = find_goldbach_partition(n, prime_number)
    print(partitions)

~~~