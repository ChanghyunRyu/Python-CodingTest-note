## 조이스틱

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42860

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.
~~~
▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
~~~
예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
~~~
- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
~~~

만들고자 하는 이름 name이 매개변수로 주어질 때, 
이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

---
### Problem Solved Check
- [x] 1회  24/08/14
- [ ] 2회
- [ ] 3회
~~~
import heapq


def solution(name):
    change_character = 0
    targets = set()
    for i in range(len(name)):
        step_forward = ord(name[i])-ord('A')
        step_backward = abs(26-step_forward)
        change_character += min(step_forward, step_backward)
        if step_forward != 0:
            targets.add(i)

    queue = [(0, 0, targets)]
    while queue:
        result, now, targets = heapq.heappop(queue)
        if not targets:
            break
        for target in targets:
            new_targets = set(targets)
            new_targets.remove(target)
            forward = abs(target-now)
            backward = abs(len(name)-forward)
            heapq.heappush(queue, (result+min(forward, backward), target, new_targets))
    return change_character+result
    
~~~