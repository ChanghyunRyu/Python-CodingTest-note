import sys
n = int(input())
wines = []
for i in range(n):
    wines.append(int(sys.stdin.readline()))
scores = [0]*n
scores[0] = wines[0]
if n > 1:
    scores[1] = wines[0] + wines[1]
if n > 2:
    scores[2] = max(wines[0] + wines[2], wines[1] + wines[2], wines[0]+wines[1])
for i in range(3, n):
    scores[i] = max(scores[i-2] + wines[i], scores[i-3] + wines[i-1] + wines[i])
    scores[i] = max(scores[i], scores[i-1])
print(scores[n-1])
