def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    return answer


def check_place(place):
    for i in range(len(place)):
        for j in range(len(place[i])):
            if not check_distance(i, j, place):
                return 0
    return 1


def check_distance(x, y, place):
    if place[x][y] != 'P':
        return True
    # 1칸 오른쪽, 아래 검사
    nx, ny = x+1, y
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P':
            return False
    nx, ny = x, y+1
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P':
            return False
    # 2칸 오른쪽, 아래 검사
    nx, ny = x+2, y
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P' and place[nx-1][ny] != 'X':
            return False
    nx, ny = x, y+2
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P' and place[nx][ny-1] != 'X':
            return False
    # 아래-오른쪽, 아래-왼쪽 검사
    nx, ny = x+1, y+1
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P' and (place[nx-1][ny] == 'O' or place[nx][ny-1] == 'O'):
            return False
    nx, ny = x+1, y-1
    if 0 <= nx < len(place) and 0 <= ny < len(place[0]):
        if place[nx][ny] == 'P' and (place[nx-1][ny] == 'O' or place[nx][ny+1] == 'O'):
            return False
    return True


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
