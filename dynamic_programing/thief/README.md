## 도둑질

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42897

도둑이 어느 마을을 털 계획을 하고 있습니다. 
이 마을의 모든 집들은 동그랗게 배치되어 있습니다.

각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에 인접한 두 집을 털면 경보가 울립니다.

각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return 하도록 solution 함수를 작성하세요.

### 제한 사항

- 이 마을에 있는 집은 3개 이상 1,000,000개 이하입니다.
- money 배열의 각 원소는 0 이상 1,000 이하인 정수입니다.

---
### Problem Solved Check
- [x] 1회 24/08/13 
- [ ] 2회
- [ ] 3회
~~~
def solution(money):
    dp_start_one = [0]*(len(money)-1)
    dp_start_one[0] = dp_start_one[1] = money[0]
    for i in range(2, len(money)-1):
        dp_start_one[i] = max(dp_start_one[i-1], dp_start_one[i-2]+money[i])

    dp_start_two = [0]*len(money)
    dp_start_two[0] = 0
    dp_start_two[1] = money[1]
    for i in range(2, len(money)):
        dp_start_two[i] = max(dp_start_two[i-1], dp_start_two[i-2]+money[i])
    
    return max(dp_start_one[-1], dp_start_two[-1])
    
~~~
~~~
def solution(money):
    dp_start_one = money[0] + get_max_return(money[2:len(money)-1])
    dp_start_two = money[1] + get_max_return(money[3:])
    dp_start_three = money[2] + get_max_return(money[4:]+[money[0]])
    return max(dp_start_one, dp_start_two, dp_start_three)


def get_max_return(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    dp = [0]*len(arr)
    dp[0] = arr[0]
    dp[1] = arr[1]
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-2]+arr[i], dp[i-1])
    return dp[-1]
    
~~~