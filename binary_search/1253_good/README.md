## 1253번 좋다

---

시간 제한: 2초, 메모리 제한: 256MB

N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.

N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.

수의 위치가 다르면 값이 같아도 다른 수이다.

### 입력

- 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 
- 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)

### 출력

- 좋은 수의 개수를 첫 번째 줄에 출력한다.
---
### Problem Solved Check
- [x] 1회 24/05/22
- [ ] 2회
- [ ] 3회

문제에서 숫자를 정렬하여 준다는 조건이 없었는데 이분 탐색을 바로 사용하여 틀린 판정을 받았다.
~~~
n = int(input())
nums = list(map(int, input().split()))
# 이분 탐색은 항상 정렬된 상태에서 사용!!
nums.sort()


def bisearch(target, numbers):
    for i in range(len(numbers)):
        start = i+1
        end = len(numbers)-1
        while start <= end:
            mid = (start+end)//2
            if numbers[i]+numbers[mid] == target:
                return True
            elif numbers[i]+numbers[mid] > target:
                end = mid-1
            else:
                start = mid+1
    return False


count = 0
for j in range(n):
    if bisearch(nums[j], nums[:j]+nums[j+1:]):
        count += 1
print(count)

~~~