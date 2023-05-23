import sys
from collections import deque

queue = deque([])

n = int(input())
while True:
    packet = int(sys.stdin.readline())
    if packet == -1:
        break
    elif packet == 0:
        queue.popleft()
    else:
        if len(queue) < n:
            queue.append(packet)
if queue:
    for p in queue:
        print(p, end=' ')
else:
    print('empty')
