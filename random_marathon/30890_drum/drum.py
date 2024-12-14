x, y = map(int, input().split())

end = x*y
result = []
for i in range(1, end+1):
    if i % x == 0 and i % y == 0:
        result.append('3')
    elif i % x == 0:
        result.append('2')
    elif i % y == 0:
        result.append('1')
result = int(''.join(result))
print(result)
