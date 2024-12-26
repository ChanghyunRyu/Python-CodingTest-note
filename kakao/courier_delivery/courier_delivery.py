def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries or pickups:
        while deliveries and pickups and deliveries[-1] == 0 and pickups[-1] == 0:
            deliveries.pop()
            pickups.pop()
        distance = max(len(deliveries), len(pickups))
        answer += 2*distance

        dt = 0
        while deliveries:
            dt += deliveries.pop()
            if dt > cap:
                deliveries.append(dt-cap)
                break

        pt = 0
        while pickups:
            pt += pickups.pop()
            if pt > cap:
                pickups.append(pt-cap)
                break
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7 ,[1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(2, 2, [0, 6], [0, 0]))
