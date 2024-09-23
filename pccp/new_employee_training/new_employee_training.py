import heapq


def solution(ability, number):
    q = []
    for a in ability:
        heapq.heappush(q, a)

    for _ in range(number):
        e1 = heapq.heappop(q)
        e2 = heapq.heappop(q)
        heapq.heappush(q, e1+e2)
        heapq.heappush(q, e1+e2)
    return sum(q)


print(solution([10, 3, 7, 2], 2))
print(solution([1, 2, 3, 4], 3))
