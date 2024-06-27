n, b = input().split()
b = int(b)

result = 0
for i in range(len(n)-1, -1, -1):
    if n[i].isdigit():
        result += (b**(len(n)-i-1))*int(n[i])
    else:
        result += (b**(len(n)-i-1))*(ord(n[i])-55)

print(result)
