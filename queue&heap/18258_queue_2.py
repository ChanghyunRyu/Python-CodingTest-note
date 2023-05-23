# 파이썬에서 del 명령어를 통해 배열을 가장 앞 인덱스를 지우는 경우,
# 배열을 앞으로 땡겨야되기 시간이 오래 걸린다는 점을 알게 되었습니다.
import sys
from collections import deque

queue = deque([])

n = int(input())
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
