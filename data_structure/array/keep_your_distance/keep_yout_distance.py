def solution(places):
    answer = []
    for place in places:
        result = 1
        end = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    if i+1 < 5 and place[i+1][j] == 'P':
                        result = 0
                        end = True
                    if i+2 < 5 and place[i+1][j] != 'X' and place[i+2][j] == 'P':
                        result = 0
                        end = True
                    if i+1 < 5 and j+1 < 5 and place[i+1][j+1] == 'P' and (place[i+1][j] != 'X' or place[i][j+1] != 'X'):
                        result = 0
                        end = True
                    if j-1 >= 0 and i+1 < 5 and place[i+1][j-1] == 'P' and (place[i+1][j] != 'X' or place[i][j-1] != 'X'):
                        result = 0
                        end = True
                    if j+1 < 5 and place[i][j+1] == 'P':
                        result = 0
                        end = True
                    if j+2 < 5 and place[i][j+1] != 'X' and place[i][j+2] == 'P':
                        result = 0
                        end = True
                if end:
                    break
            if end:
                break
        answer.append(result)
    return answer
