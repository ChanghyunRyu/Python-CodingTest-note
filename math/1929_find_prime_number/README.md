## 1929번 소수 구하기

---

시간 제한: 2초, 메모리 제한: 256MB

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) 
- M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

### 출력

- 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

---
~~~
m, n = map(int, input().split())


def find_prime_number(start, number):
    is_prime = [True]*(number+1)
    is_prime[1] = False
    end = int((number+1)**0.5)
    for i in range(2, end+1):
        if is_prime[i]:
            for j in range(i+i, number+1, i):
                is_prime[j] = False
    return [i for i in range(start, number+1) if is_prime[i]]


prime_numbers = find_prime_number(m, n)
for prime_number in prime_numbers:
    print(prime_number)

~~~