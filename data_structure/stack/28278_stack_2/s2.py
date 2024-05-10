import sys
from collections import deque

n = int(input())
s = deque()
for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        s.append(command[1])
    elif command[0] == 2:
        if s:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(s))
    elif command[0] == 4:
        if s:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if s:
            num = s.pop()
            print(num)
            s.append(num)
        else:
            print(-1)
