## 1735번 분수 합

---

시간 제한: 2초, 메모리 제한: 128MB

분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.

두 분수의 합 또한 분수로 표현할 수 있다. 
두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 
기약분수란 더 이상 약분되지 않는 분수를 의미한다.

### 입력

- 첫째 줄과 둘째 줄에, 각 분수의 분자와 분모를 뜻하는 두 개의 자연수가 순서대로 주어진다. 
- 입력되는 네 자연수는 모두 30,000 이하이다.

### 출력

- 첫째 줄에 구하고자 하는 기약분수의 분자와 분모를 뜻하는 두 개의 자연수를 빈 칸을 사이에 두고 순서대로 출력한다.

---
최대공약수를 구할 때는 유클리드 호제법을 이용하는 것이 좋다.
~~~
def find_least_common_multiple(n1, n2):
    mul1, mul2 = n1, n2
    while n1 != n2:
        if n1 > n2:
            n2 += mul2
        else:
            n1 += mul1
    return n1


def find_greatest_common_divisor(n1, n2):
    while n1 % n2 != 0 and n2 % n1 != 0:
        if n1 > n2:
            n1 %= n2
        else:
            n2 %= n1
    return min(n1, n2)


num1, deno1 = map(int, input().split())
num2, deno2 = map(int, input().split())
lcm = find_least_common_multiple(deno1, deno2)
num_sum = num1*(lcm//deno1) + num2*(lcm//deno2)
gcd = find_greatest_common_divisor(lcm, num_sum)
print('{} {}'.format(num_sum//gcd, lcm//gcd))

~~~