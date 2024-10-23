import sys


def check_runway(line, need):
    check = [False]*len(line)
    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            continue
        elif abs(line[i]-line[i+1]) > 1:
            return False
        # 경사로 설치할 수 있는지 체크
        if line[i] > line[i+1]:
            for step in range(1, need+1):
                ni = i+step
                if ni >= len(line):
                    return False
                if not check[ni]:
                    check[ni] = True
                else:
                    return False
        else:
            for step in range(1, need+1):
                ni = i-need+step
                if ni < 0:
                    return False
                if not check[ni]:
                    check[ni] = True
                else:
                    return False
    return True


n, runway = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

answer = 0
for line in board:
    if check_runway(line, runway):
        answer += 1

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(board[j][i])
    if check_runway(temp, runway):
        answer += 1
print(answer)
