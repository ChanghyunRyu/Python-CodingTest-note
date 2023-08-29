import sys
meeting = []
n = int(input())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((start, end))
meeting.sort(key=lambda x: (x[1], x[0]))

result = 0
end = 0
for m in meeting:
    if m[0] >= end:
        result += 1
        end = m[1]
print(result)
