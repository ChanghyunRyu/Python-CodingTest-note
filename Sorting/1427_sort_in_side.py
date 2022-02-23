data = list(input())
data = [int(i) for i in data]
data.sort(reverse=True)
for num in data:
    print(num, end='')
