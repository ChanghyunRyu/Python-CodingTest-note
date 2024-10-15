## 타겟 넘버

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/43165

n개의 음이 아닌 정수들이 있습니다. 
이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
~~~
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
~~~

사용할 수 있는 숫자가 담긴 배열 numbers, 
타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

---
### Problem Solved Check
- [X] 1회 24/07/27  
- [X] 2회 24/10/15
- [ ] 3회
~~~
import sys
sys.setrecursionlimit(int(1e8))


def solution(numbers, target):
    answer = get_target(numbers, target)
    return answer


def get_target(numbers, target):
    if len(numbers) == 1:
        if numbers[0] == target or numbers[0] == -target:
            return 1
        else:
            return 0
    return get_target(numbers[1:], target-numbers[0]) + get_target(numbers[1:], target+numbers[0])
~~~
~~~
def solution(numbers, target):
    answer = 0
    stack = [(0, 0)]
    while stack:
        now, idx = stack.pop()
        if idx == len(numbers)-1:
            if now+numbers[idx] == target or now-numbers[idx] == target:
                answer += 1
            continue
        stack.append((now+numbers[idx], idx+1))
        stack.append((now-numbers[idx], idx+1))
    return answer
~~~