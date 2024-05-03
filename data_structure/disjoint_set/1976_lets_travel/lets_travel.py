import sys


def find_parent(x, p):
    if p[x] != x:
        p[x] = find_parent(p[x], p)
    return p[x]


def union_parent(a, b, p):
    a = find_parent(a, p)
    b = find_parent(b, p)
    if a < b:
        p[b] = a
    else:
        p[a] = b


n = int(input())
m = int(input())
parent = [0]*n
for i in range(n):
    parent[i] = i
cnt = 0
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for i in range(len(line)):
        if line[i] == 1 and find_parent(cnt, parent) != find_parent(i, parent):
            union_parent(cnt, i, parent)
    cnt += 1

result = True
question = list(map(int, sys.stdin.readline().split()))
main_parent = parent[question[0]-1]
for q in question:
    if main_parent != parent[q-1]:
        result = False
        break
if result:
    print("YES")
else:
    print("NO")