## 2565번 전깃줄

---

시간 제한: 1초, 메모리 제한: 256MB

두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.

전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에는 두 전봇대 사이의 전깃줄의 개수가 주어진다. 전깃줄의 개수는 100 이하의 자연수이다. 
- 둘째 줄부터 한 줄에 하나씩 전깃줄이 A전봇대와 연결되는 위치의 번호와 B전봇대와 연결되는 위치의 번호가 차례로 주어진다. 
- 위치의 번호는 500 이하의 자연수이고, 같은 위치에 두 개 이상의 전깃줄이 연결될 수 없다.

### 출력

- 첫째 줄에 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수를 출력한다.

---

전깃줄 A, B가 있다고 했을 때, 두 전깃줄이 꼬여있다는 것은 A[0], B[0] 의 대소관계와 A[1], B[1] 의 대소관계가 다르다는 것이다.  
즉, 두 전깃줄이 교차되지 않기위해서는 A[0] < B[0] 일때 A[1] < B[1] 역시 성립해야한다.  

따라서 시작점 혹은 끝점을 기준으로 전깃줄을 오름차순으로 정렬했을 때, 반대쪽도 오름차순으로 정렬되어야 한다. 
결국 시작점을 기준으로 전깃줄 들을 정렬한 후, 끝점을 기준으로 최장 증가 수열을 찾으면 교차하지 않는 가장 많은 전깃줄의 수가 된다.

~~~
import sys


def binary_search(target, arr):
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start+end)//2
        if target > arr[mid]:
            start = mid+1
        else:
            end = mid
    return end


n = int(input())
cords = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    cords.append((a, b))
cords.sort()

dp = [0]*n
dp[0] = 1
A = [cords[0][1]]
for i in range(1, len(cords)):
    _, num = cords[i]
    if num > A[len(A)-1]:
        A.append(num)
        dp[i] = len(A)
    else:
        pos = binary_search(num, A)
        dp[i] = dp[pos]
        if A[pos] > num:
            A[pos] = num
print(n-len(A))

~~~

Python bisect를 이용하는 방법

~~~
import sys
from bisect import bisect_left

n = int(input())
cords = []
for _ in range(n):
    cords.append(list(map(int, sys.stdin.readline().split())))
cords.sort()

dp = [0]*n
dp[0] = 1
A = [cords[0][1]]
for i in range(1, n):
    _, num = cords[i]
    if num > A[len(A)-1]:
        A.append(num)
        dp[i] = len(A)
    else:
        pos = bisect_left(A, num)
        dp[i] = pos
        if A[pos] > num:
            A[pos] = num
print(n-len(A))

~~~