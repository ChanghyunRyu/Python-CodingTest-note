# 1, 1, 1, 2, 2
# 3(2+1), 4(3+1), 5(4+1), 7(5+2), 9(5+2), 12(9+3)
import sys

t = int(input())
n = []
for i in range(t):
    n.append(int(sys.stdin.readline()))
triangles = [1]*100
triangles[3] = triangles[4] = 2
for i in range(5, 100):
    triangles[i] = triangles[i-1] + triangles[i-5]

for num in n:
    print(triangles[num-1])
