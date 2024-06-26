def solution(m, n, puddles):
    way = [[0]*m for _ in range(n)]
    way[0][0] = 1
    for puddle in puddles:
        x, y = puddle[0]-1, puddle[1]-1
        way[y][x] = -1
    for p_y in range(len(way)):
        for p_x in range(len(way[p_y])):
            if way[p_y][p_x] == -1:
                continue
            if p_y-1 >= 0 and way[p_y-1][p_x] != -1:
                way[p_y][p_x] += way[p_y-1][p_x]
            if p_x-1 >= 0 and way[p_y][p_x-1] != -1:
                way[p_y][p_x] += way[p_y][p_x-1]
    print(way)
    return way[-1][-1] % 1000000007


print(solution(4, 3, [[2, 2]]))
