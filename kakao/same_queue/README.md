## 두 큐 합 같게 만들기

---

[문제]https://school.programmers.co.kr/learn/courses/30/lessons/118667

문제를 읽고 기본적인 알고리즘을 짜는 건 굉장히 쉬운 문제.

단지 단순히 그대로 알고리즘을 짜는 경우, 큐1과 큐2에서 순환이 일어나는 경우 탈출할 수 없어 시간초과가 발생하게 된다.
처음에는 딕셔너리를 통해 큐의 형태를 기억해서 풀까 했는데 큐의 길이가 너무 커서 딕셔너리에 들어가는 형태로 만들어버리면 오히려 시간이 더 걸린다.

결국 모든 원소 합의 갯수를 구해보는 시간복잡도를 계산해서 그 시간복잡도를 넘어가면 탈출하는 것으로 해결.

~~~
from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    n = len(queue1)
    while sum1 != sum2:
        if not queue1 or not queue2 or answer > 3*n:
            answer = -1
            break
        answer += 1
        if sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
        else:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
    return answer
~~~
