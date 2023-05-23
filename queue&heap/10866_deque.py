import sys
from collections import deque

n = int(input())
data = deque([])

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        data.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        data.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(data) > 0:
            print(data.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(data) > 0:
            print(data.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(data))
    elif command[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(data) > 0:
            print(data[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(data) > 0:
            print(data[len(data)-1])
        else:
            print(-1)
