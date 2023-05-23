import sys
from collections import deque

result = []
test = int(input())
for t in range(test):
    # direction: 1(정방향), -1(역방향)
    direction = 1
    command = sys.stdin.readline().strip()
    n = int(input())
    data = sys.stdin.readline().strip()
    if n != 0:
        data = deque(list(map(int, data[1:len(data)-1].split(','))))
    else:
        data = deque([])
    error_flag = False

    for c in command:
        if c == 'R':
            direction *= -1
        elif c == 'D':
            if len(data) > 0:
                if direction == 1:
                    data.popleft()
                else:
                    data.pop()
            else:
                error_flag = True
                break
    data = list(data)
    if error_flag:
        print('error')
    else:
        if direction == -1:
            data.reverse()
        print('[', end='')
        for i in range(len(data)):
            if i != len(data)-1:
                print(data[i], end=',')
            else:
                print(data[i], end='')
        print(']')


