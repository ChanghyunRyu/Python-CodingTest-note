import sys

n = int(sys.stdin.readline().rstrip())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, sys.stdin.readline().split())))
meeting.sort(key=lambda x: (x[1], x[0]))
spend = 0
count = 0
for m in meeting:
    start, end = m
    if start >= spend:
        spend = end
        count += 1
print(count)
