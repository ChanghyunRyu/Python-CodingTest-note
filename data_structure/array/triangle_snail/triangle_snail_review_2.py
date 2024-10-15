def solution(n):
    direction = [[1, 0], [0, 1], [-1, -1]]
    snail = [[0]*(i+1) for i in range(n)]

    count = n
    point = [-1, 0]
    idx = 0
    num = 0
    while count != 0:
        for _ in range(count):
            num += 1
            point[0] += direction[idx][0]
            point[1] += direction[idx][1]
            snail[point[0]][point[1]] = num
        count -= 1
        idx = (idx+1) % 3
    return sum(snail, [])


print(solution(4))
print(solution(5))
print(solution(6))
