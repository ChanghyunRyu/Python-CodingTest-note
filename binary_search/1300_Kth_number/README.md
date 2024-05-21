## 1300번 K번째 수

---

시간 제한: 2초, 메모리 제한: 128MB

세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다.

### 입력

- 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 
- 둘째 줄에 k가 주어진다. k는 min(10^9, N^2)보다 작거나 같은 자연수이다.

### 

- B[k]를 출력한다.
---
### Problem Solved Check
- [x] 1회 24/05/21
- [ ] 2회
- [ ] 3회

임의의 수 A를 선정하고 그 A라는 숫자보다 작은 숫자가 해당 배열 안에 몇개가 있는지를 체크하는 문제이다.  

A보다 작은 수의 개수가 몇 개인지를 어떻게 구하는지에 대하여 생각할 수 있어야 한다.
~~~
n = int(input())
k = int(input())

start = 0
end = n*n
result = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(1, n+1):
        count += min(n, mid//i)
    if count >= k:
        result = mid
        end = mid-1
    else:
        start = mid+1
print(result)

~~~