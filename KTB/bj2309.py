from itertools import combinations


dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

answer = []
for combination in combinations(dwarf, 7):
    if sum(combination) == 100:
        answer = list(combination)
        break

answer.sort()
for d in answer:
    print(d)
