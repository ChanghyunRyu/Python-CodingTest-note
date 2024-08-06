  ## 징검다리

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/43236

출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 
바위 중 몇 개를 제거하려고 합니다.  
예를 들어, 도착지점이 25만큼 떨어져 있고, 
바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 
바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

|제거한 바위의 위치|각 바위 사이의 거리| 거리의 최솟값 |
|-|-|---------|
|[21, 17]|[2, 9, 3, 11]| 2       |
|[2, 21]|	[11, 3, 3, 8]| 3       |
|[2, 11]|	[14, 3, 4, 4]| 3       |
|[11, 21]|[2, 12, 3, 8]| 2       |
|[2, 14]|	[11, 6, 4, 4]| 4       |

위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발 지점부터 도착 지점까지의 거리 distance, 
바위들이 있는 위치를 담은 배열 rocks, 
제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 
각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
- 바위는 1개 이상 50,000개 이하가 있습니다.
- n 은 1 이상 바위의 개수 이하입니다.

---
### Problem Solved Check
- [x] 1회 24/06/20
- [x] 2회 24/08/06
- [ ] 3회

~~~
from bisect import bisect_left


def solution(distance, rocks, n):
    rocks.sort()
    range_rocks = rocks[:bisect_left(rocks, distance)]
    range_rocks.append(distance)

    start = 0
    end = distance
    while start <= end:
        mid = (start+end)//2
        if chk_length(range_rocks, mid, n):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def chk_length(rocks, length, n):
    stack = [0]
    count = 0
    for r in rocks:
        now = r - stack[-1]
        if now < length:
            count += 1
            if count > n:
                return False
        else:
            stack.append(r)
    return True
    
~~~
~~~
def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    answer = 0
    start, end = 0, distance
    while start <= end:
        mid = (start+end)//2
        if check_distance(mid, rocks, n):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def check_distance(distance, rocks, n):
    before_rock = 0
    chance = n
    for rock in rocks:
        dis = rock-before_rock
        if dis < distance:
            if chance > 0:
                chance -= 1
                continue
            else:
                return False
        before_rock = rock
    return True
    
~~~
