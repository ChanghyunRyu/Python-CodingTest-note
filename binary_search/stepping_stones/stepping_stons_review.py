def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    answer = 0
    start, end = 0, distance
    while start <= end:
        mid = (start+end)//2
        if check_distance(mid, rocks, n):
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer


def check_distance(distance, rocks, n):
    before_rock = 0
    chance = n
    for rock in rocks:
        dis = rock-before_rock
        if dis < distance:
            if chance > 0:
                chance -= 1
                continue
            else:
                return False
        before_rock = rock
    return True


print(solution(25, [2, 14, 11, 21, 17], 2))
