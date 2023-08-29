n = int(input())
result = -1
for i in range((n//3)+1):
    if (n-i*3)%5 == 0:
        result = i + (n-i*3)//5
        break
print(result)
