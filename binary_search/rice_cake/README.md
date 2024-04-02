## 떡볶이 떡 만들기

---

시간제한: 2초, 메모리 제한: 128MB

### 입력

- 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.(1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
- 둘째 줄에는 떡의 개별 높이가 주어진다.
- 떡 높이의 총합은 항상 M 이상으므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
- 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

### 출력

- 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

### 설명

- 이진 탐색 문제이자, Parametric Search 유형의 문제이다. 파라메트릭 서치는 최적화 문제를 결정문제로 바꾸어 해결하는 기법이다.
- 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 파라메트릭 서치를 사용한다.

~~~
n, m = map(int, input().split())
ricecake = list(map(int, input().split()))
ricecake.sort()
start, end = 0, ricecake[len(ricecake)-1]

while start < end:
    mid = (start+end)//2
    sum = 0
    for r in ricecake:
        if r > mid:
            sum += r - mid
    if sum < m:
        start, end = start, mid-1
    elif sum == m:
        break
    else:
        start, end = mid+1, end

print(mid)

~~~
