## 하노이의 탑

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/12946

하노이 탑(Tower of Hanoi)은 퍼즐의 일종입니다. 
세 개의 기둥과 이 기동에 꽂을 수 있는 크기가 다양한 원판들이 있고, 
퍼즐을 시작하기 전에는 한 기둥에 원판들이 작은 것이 위에 있도록 순서대로 쌓여 있습니다. 
게임의 목적은 다음 두 가지 조건을 만족시키면서, 
한 기둥에 꽂힌 원판들을 그 순서 그대로 다른 기둥으로 옮겨서 다시 쌓는 것입니다.

1. 한 번에 하나의 원판만 옮길 수 있습니다.
2. 큰 원판이 작은 원판 위에 있어서는 안됩니다.

하노이 탑의 세 개의 기둥을 왼쪽 부터 1번, 2번, 3번이라고 하겠습니다. 
1번에는 n개의 원판이 있고 이 n개의 원판을 3번 원판으로 최소 횟수로 옮기려고 합니다.

1번 기둥에 있는 원판의 개수 n이 매개변수로 주어질 때, 
n개의 원판을 3번 원판으로 최소로 옮기는 방법을 return하는 solution를 완성해주세요.

### 제한 사항

- n은 15이하의 자연수 입니다.

---
### Problem Solved Check
- [x] 1회 24/06/07
- [ ] 2회
- [ ] 3회

하노이 타워는 유명한 재귀 함수 문제 중 하나이다.  

탑 세개를 각각 1, 2, 3번 탑이라고 정하고 생각하면  
n개의 원반을 가진 하노이 타워를 1→3 으로 옮기는 과정은 
n-1개의 원반을 1→2로 옮긴 후 가장 큰 원반을 1 → 3 옮긴다.  

이렇게 되면 1~n-1까지의 원반은 2번에 가장 큰 원반은 3번에 있게 되고 이는 2번탑을 1번탑이라고 
가정하면 n-1개의 원반을 옮기는 하노이 타워 문제가 된다.
이를 통하여 재귀 함수로 문제를 해결하면 된다.

~~~
def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer


def hanoi(result, num, start, mid, end):
    if num == 1:
        result.append([start, end])
    else:
        hanoi(result, num-1, start, end, mid)
        result.append([start, end])
        hanoi(result, num-1, mid, start, end)
        
~~~
