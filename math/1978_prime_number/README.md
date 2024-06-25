## 1978번 소수 찾기

---

시간 제한: 2초, 메모리 제한: 128MB

주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

### 입력

- 첫 줄에 수의 개수 N이 주어진다. 
- N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

### 출력

- 주어진 수들 중 소수의 개수를 출력한다.

---
~~~
n = int(input())
nums = list(map(int, input().split()))

prime_number = {}
limit = max(nums)
for i in range(2, limit+1):
    is_prime = True
    for p in prime_number:
        if i % p == 0:
            is_prime = False
            break
    if is_prime:
        prime_number[i] = True

count = 0
for n in nums:
    if n in prime_number:
        count += 1

print(count)

~~~
