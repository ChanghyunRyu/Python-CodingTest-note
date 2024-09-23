def solution(menu, order, k):
    waiting = [0]*1000000
    last = 0
    for i in range(len(order)):
        start = k*i
        waiting[start] += 1
        last = max(last, start) + menu[order[i]]
        waiting[last] -= 1
    for i in range(1, len(waiting)):
        waiting[i] += waiting[i-1]
    return max(waiting)


print(solution([5, 12, 30], [1, 2, 0, 1], 10))
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))
print(solution([5], [0, 0, 0, 0, 0], 5))
print(solution([5, 6, 7, 11], [1, 2, 3, 3, 2, 1, 1], 10))
