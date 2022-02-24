n = int(input())
data_a = list(map(int, input().split()))
m = int(input())
data_b = list(map(int, input().split()))

data_a = set(data_a)

for num in data_b:
    if num in data_a:
        print('1')
    else:
        print('0')
