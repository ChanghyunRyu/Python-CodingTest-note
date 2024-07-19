def solution(places):
    answer = []
    for p in places:
        answer.append(check_place_distance(p))
    return answer


def check_place_distance(place):
    for i in range(len(place)):
        for j in range(len(place[i])):
            if check_distance(i, j, place):
                return 0
    return 1


def check_distance(x, y, arr):
    if arr[x][y] != 'P':
        return False
    len_x = len(arr)
    len_y = len(arr[0])
    if x+1 < len_x and arr[x+1][y] == 'P':
        return True
    if y+1 < len_y and arr[x][y+1] == 'P':
        return True
    if x+2 < len_x and arr[x+1][y] == 'O' and arr[x+2][y] == 'P':
        return True
    if y+2 < len_y and arr[x][y+1] == 'O' and arr[x][y+2] == 'P':
        return True
    if x+1 < len_x and y+1 < len_y and arr[x+1][y+1] == 'P' and (arr[x][y+1] == 'O' or arr[x+1][y] == 'O'):
        return True
    if x+1 < len_x and y-1 >= 0 and arr[x+1][y-1] == 'P' and (arr[x+1][y] == 'O' or arr[x][y-1] == 'O'):
        return True
    return False


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
                ["OOOOO", "OOOOO", "OPOPO", "OOOOO", "OOOOO"]
                ]))
