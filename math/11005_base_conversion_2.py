n, b = map(int, input().split())

result = []
while n >= b:
    n, remainder = n//b, n % b
    if remainder > 9:
        remainder = chr(remainder+55)
    else:
        remainder = str(remainder)
    result.append(remainder)
else:
    if n > 9:
        n = chr(n+55)
    else:
        n = str(n)
    result.append(n)

result.reverse()
print(''.join(result))
