import heapq


def solution(program):
    answer = [0]*11
    q = []
    program = sorted(program, key=lambda x: (x[1], x[0]), reverse=True)
    now = 0
    while q or program:
        if not q:
            heapq.heappush(q, program.pop())
        score, start, time = heapq.heappop(q)
        if now > start:
            answer[score] += now-start
        now = max(now, start) + time
        while program:
            if program[-1][1] > now:
                break
            heapq.heappush(q, program.pop())
    answer[0] = now
    return answer


print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))
