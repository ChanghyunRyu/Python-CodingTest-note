import sys
from collections import deque
from collections import defaultdict


n, m, k = map(int, input().split())
nutrients = [[5]*n for _ in range(n)]
s2d2 = []
for _ in range(n):
    s2d2.append(list(map(int, sys.stdin.readline().split())))

trees = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, sys.stdin.readline().split())
    trees[x-1][y-1].append(age)
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]


def tree_investment():
    # spring
    dead = defaultdict(list)
    breeding = []
    for i in range(n):
        for j in range(n):
            tree = trees[i][j]
            new_tree = deque()
            while tree:
                age = tree.popleft()
                if nutrients[i][j] >= age:
                    nutrients[i][j] -= age
                    if (age+1) % 5 == 0:
                        breeding.append((i, j))
                    new_tree.append(age+1)
                else:
                    tree.append(age)
                    dead[(i, j)] = list(tree)
                    break
            trees[i][j] = new_tree
            # winter
            nutrients[i][j] += s2d2[i][j]
    # summer
    for key in dead:
        for t in dead[key]:
            nutrients[key[0]][key[1]] += t//2
    # autumn
    for b in breeding:
        for i in range(8):
            nx = b[0] + dx[i]
            ny = b[1] + dy[i]
            check = 0 <= nx < len(nutrients) and 0 <= ny < len(nutrients)
            if check:
                trees[nx][ny].appendleft(1)


for _ in range(k):
    tree_investment()

answer = 0
for r in range(n):
    for c in range(n):
        answer += len(trees[r][c])
print(answer)
