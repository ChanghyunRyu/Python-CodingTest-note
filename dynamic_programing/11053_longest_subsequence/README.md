## 11053번 가장 긴 증가하는 부분 수열

---

시간 제한: 1초, 메모리 제한: 256MB

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

### 입력

- 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
- 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

### 출력

- 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

---

### Problem Solved Check

- [x] 1회
- [ ] 2회
- [ ] 3회

~~~
n = int(input())
A = list(map(int, input().split()))


def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid
    return end


dp = [0]*n
B = [A[0]]
for i in range(1, n):
    if A[i] > B[len(B)-1]:
        B.append(A[i])
        dp[i] = len(B)
    else:
        pos = binary_search(A[i], B)
        dp[i] = pos
        if A[i] < B[pos]:
            B[pos] = A[i]
print(len(B))

~~~