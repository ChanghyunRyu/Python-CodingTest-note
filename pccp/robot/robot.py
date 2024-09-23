def solution(command):
    answer = [0, 0]
    nxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    idx = 0
    for c in command:
        if c == 'G':
            answer[0] += nxy[idx][0]
            answer[1] += nxy[idx][1]
        elif c == 'B':
            answer[0] -= nxy[idx][0]
            answer[1] -= nxy[idx][1]
        elif c == 'R':
            idx = (idx+1) % 4
        elif c == 'L':
            idx = (idx-1) % 4
    return answer


print(solution("GRGLGRG"))
print(solution("GRGRGRB"))
