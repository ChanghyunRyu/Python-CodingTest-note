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

