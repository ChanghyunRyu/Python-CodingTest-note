a, b, c, d, e, f = map(int, input().split())

escape_x = False
for x in range(1999):
    for y in range(1999):
        if a*(x-999) + b*(y-999) == c and d*(x-999) + e*(y-999) == f:
            result = [x, y]
            escape_x = True
            break
    if escape_x:
        break

print('{} {}'.format(result[0]-999, result[1]-999))
