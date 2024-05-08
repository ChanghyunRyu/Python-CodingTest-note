# 계단 오르기와 비슷하면서 다른 문제이다.
# 계단 오르기에서 영감을 받아 스코어를 구하는 것까지는 동일하게 했으나 마지막에 max(score[n-1], score[n-2])를 하는 것이 처음 해결이였다.
# 그러나 이후, 마지막 스코어 당시가 아니라 계산 과정에서 해당 작업을 해줘야 한다는 것을 깨달아 수정하여 해결하였다.
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
