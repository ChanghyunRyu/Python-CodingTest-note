n = int(input())
plan = input().split()
x, y = 1, 1

for i in range(len(plan)):
    if plan[i] == 'R':
        if y < 5:
            y += 1
    elif plan[i] == 'L':
        if y > 1:
            y -= 1
    elif plan[i] == 'U':
        if x > 1:
            x -= 1
    elif plan[i] == 'D':
        if x < 5:
            x += 1

print("{} {}".format(x, y))
