from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1

    q = deque()
    truck = deque(truck_weights)
    while q or truck:
        if truck and truck[0] <= weight:
            w = truck.popleft()
            weight -= w
            q.append((answer + bridge_length, w))
        answer += 1
        if q and q[0][0] == answer:
            weight += q.popleft()[1]
    return answer