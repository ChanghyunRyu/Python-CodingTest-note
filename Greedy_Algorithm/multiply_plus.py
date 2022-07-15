equation = input()
result = 0
for char in equation:
    num = int(char)
    if result == 0 or num == 0:
        result += num
    else:
        result *= num
print(result)

