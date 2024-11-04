from itertools import combinations


n, m = map(int, input().split())
cities = []
for _ in range(n):
    cities.append(list(map(int, input().split())))

chickens = []
homes = []
for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            homes.append((i, j))
        elif cities[i][j] == 2:
            chickens.append((i, j))


def get_distance(chicken, home):
    distance = [101]*len(home)
    for c in chicken:
        for i in range(len(home)):
            new_distance = abs(c[0]-home[i][0])+abs(c[1]-home[i][1])
            distance[i] = min(distance[i], new_distance)
    return sum(distance)


answer = int(1e9)
for com in combinations(chickens, m):
    answer = min(answer, get_distance(com, homes))
print(answer)
