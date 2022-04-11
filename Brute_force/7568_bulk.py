n = int(input())
bulks = []
for i in range(n):
    weight, height = map(int, input().split())
    bulks.append((weight, height))

ranks = []
for bulk in bulks:
    count = 0
    for bulk2 in bulks:
        if bulk[0] < bulk2[0] and bulk[1] < bulk2[1]:
            count += 1
    ranks.append(count+1)
for rank in ranks:
    print(rank, end=' ')
